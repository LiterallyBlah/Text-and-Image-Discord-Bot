import discord
import configparser
from textBot import TextBot
from imageBot import ImageBot

# read config file
config = configparser.ConfigParser()
config.read('config.ini')

# get values from config
bot_name = config['bot']['name']
ai_model = config['bot']['model']
discord_bot_token = config['discord']['bot_token']

# set intents
intents = discord.Intents.default()

# set discord client
client = discord.Client(intents=intents)

# create instance of TextBot
text_bot = TextBot(bot_name, ai_model)

# create instance of ImageBot
image_bot = ImageBot()

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

    # check if message is a command
    if message.content.startswith('/imagine'):
        await message.channel.send("Image generating...")

        # get prompt from message
        prompt = message.content.replace('/imagine ', '')

        # generate image based on prompt
        await image_bot.generate_image(prompt, message.channel)

    else:
        # set empty list for history
        history = []
    
        # get message history from channel
        async for m in message.channel.history(limit=1000):
            history.append(f'{m.author.name}: {m.content}')
    
        # create conversation from message history
        conversation = "\n".join(reversed(history))

        # limit conversation to 1000 characters
        conversation = conversation[-2000:]
        
        print("DEBUG CONVERSATION CONTENT:n" + conversation)
        print("DEGUG MESSAGE CONTENT:\n" + message.content)
        # get response from TextBot
        response_text = text_bot.get_response(conversation, message.content)

        # check if response is empty or null
        if response_text is None or response_text == "":
            # return if response is empty or null
            return
        # send response to channel
        await message.channel.send(response_text)


# run discord client
client.run(discord_bot_token)
