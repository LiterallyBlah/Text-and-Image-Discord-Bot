# Text and Image Discord Bot
A Discord bot that connects to GPT-3 (default model: text-davinci-003) and keeps the context of the conversation, so you can ask leading questions. There is also Dalle 2 integration where you can generate images based on the message (as long as the command is invoked).

# Configuration in config.ini
```
[openai]
api_key = INSERT_API_KEY

[bot]
name = INSERT_BOT_NAME
model = text-davinci-003

[discord]
bot_token = INSERT_BOT_TOKEN
```

# Commands
To interact with the text bot, you don't require any commands, simply type and it will respond.

To call the image bot:
`/imagine {prompt}` 

Note that I have yet to actually make it into a Discord command, so the script just checks to see if '/imagine' is in the request and uses the rest of the message as a prompt.


# Python Requirements
```
discord
configparser
openai
requests
```


# Run
Run the bot with the following terminal command:
`python3 main.py`
