# import discord and openai libraries
import discord
import openai


openai.api_key = 'INSERT_KEY_HERE' # set openai api key
discord_bot_token = 'INSERT_TOKEN_HERE' # set discord bot token
bot_name = 'ENTER_BOT_NAME' # Change to the bot name you created (i.e. Doris)
ai_model = 'text-davinci-003' # Change model to text-ada-001 if you want the fastest model

# set intents
intents = discord.Intents.all()

# set discord client
client = discord.Client(intents=intents)

# on_ready event
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')


# on_message event
@client.event
async def on_message(message):
    # check if message is from bot itself
    if message.author == client.user:
        return

    # set empty list for history
    history = []
    
    # get message history from channel
    async for m in message.channel.history(limit=1000):
        history.append(f'{m.author.name}: {m.content}')
    
    # create conversation from message history
    conversation = "\n".join(reversed(history))

    # limit conversation to 1000 characters
    if len(conversation) > 1000:
        conversation = conversation[1000:]
   

    # send conversation to openai
    response = openai.Completion.create(
        engine=ai_model,
        prompt=conversation,
        max_tokens=1500,
        temperature=0.7,
        top_p=0.5
    )

    # format response
    response_text = response['choices'][0]['text']
    response_text = response_text.replace(f"{bot_name}: ", "")
    print(conversation)

    # send response to channel
    await message.channel.send(response_text)

# run discord client
client.run(discord_bot_token)
