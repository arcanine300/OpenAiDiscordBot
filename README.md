# OpenAiDiscordBot
A simple text to image discord bot written in python using OpenAI DALL-E 2 model 

## Getting Required API Keys
* You will need to get your free OpenAI and Discord API keys in order for this bot to work. Create your Discord bot and copy the application token from [here](https://discord.com/developers/applications/). Paste the value into the `token` variable in the script. 
* Next create an account at [OpenAi.com](https://openai.com/) this step will require a phone number. After you have made your account copy your [API key](https://platform.openai.com/account/api-keys) and [Organization ID](https://platform.openai.com/account/org-settings) into the `ai.api_key` and `ai.organization` variables.

## Dependencies
* Discord-py (2.2.1): `pip install discord-py` [docs](https://discordpy.readthedocs.io/en/stable/)
* OpenAI (0.26.5): `pip install openai` [docs](https://platform.openai.com/docs/api-reference/introduction)
* aiohttp (3.8.4): `pip install aiohttp` [docs](https://pypi.org/project/aiohttp/)

## Running the Bot
Add your [Discord bot](https://discord.com/developers/applications/) to your server making sure you have given it the necessary priviliges (i.e message content, send messages, embed links, attach files) and Run the bot in any terminal with `python Txt2Img-DiscordBot.py`  

### Alternative API Key Storage
If you are planning on deploying this script you might want to consider setting up [environment variables](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety) to store your keys rather than having them in the script source code.
