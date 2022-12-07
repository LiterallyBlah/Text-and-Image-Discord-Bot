import discord
import openai

openai.api_key = "INSERT_KEY_HERE"
discord_bot_token = "INSERT_TOKEN_HERE"
bot_name = "ENTER_BOT_NAME" # Change to the bot name you created (i.e. Doris)
ai_model = "text-davinci-003" # Change model to text-ada-001 if you want the fastest model

# Change to match perms
intents = discord.Intents.all()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    history = []
    async for m in message.channel.history(limit=1000):
        history.append(f'{m.author.name}: {m.content}')
    
    conversation = "\n".join(reversed(history))
    if len(conversation) > 1000:
        conversation = conversation[1000:]
   

    response = openai.Completion.create(
        engine=ai_model,
        prompt=conversation,
        max_tokens=1900,
        temperature=0.7,
        top_p=0.5
    )

    response_text = response['choices'][0]['text']
    response_text = response_text.replace(f"{bot_name}: ", "")
    print(conversation)
    await message.channel.send(response_text)

client.run(discord_bot_token)
