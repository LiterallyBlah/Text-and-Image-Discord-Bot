import io
import requests
import discord
from PIL import Image

import configparser
import openai

class ImageBot:
    def __init__(self):
        # read config file
        config = configparser.ConfigParser()
        config.read('config.ini')

        # get api key from config
        openai.api_key = config['openai']['api_key']

    async def generate_image(self, prompt, channel):
        # send prompt to openai
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024",
            response_format="url"
        )

        # get image url from response
        image_url = response["data"][0]["url"]

        # download image
        response = requests.get(image_url)
        img = Image.open(io.BytesIO(response.content))

        # save image to file
        img.save('image.png')

        # send image to channel
        await self.send_image(channel)


    async def send_image(self, channel):
        # open image file
        with open('image.png', 'rb') as f:
            # send image to channel
            await channel.send(file=discord.File(f))
