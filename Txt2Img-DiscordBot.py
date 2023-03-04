import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import openai as ai
import random
import aiohttp
from io import BytesIO

ai.organization = "YOUR OPEN AI ORGANIZATION ID HERE" #https://platform.openai.com/account/org-settings
ai.api_key = "YOUR OPEN AI API KEY HERE" #https://platform.openai.com/account/api-keys
token = "YOUR DISCORD BOT TOKEN HERE" #https://discord.com/developers/applications/

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.guild_reactions = True
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_connect():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='Open AI'))


@bot.command()
async def create(ctx, *, request: str = commands.parameter(default="a default photo")):
  try:
    if (len(request)==0):
      request="a default photo"

    imgArr = []
    embedArr = []
    data:BytesIO
    response = ai.Image.create(prompt=request, n=4, size="512x512")

    async with aiohttp.ClientSession() as session:
      for i in response['data']:
        async with session.get(i['url']) as resp:
            data = BytesIO(await resp.read())
            filename = str(ctx.message.id + random.randint(1,99999)) + ".png"
            embed = discord.Embed(url="https://twitter.com").set_image(url="attachment://"+filename)
            embedArr.append(embed)
            imgArr.append(discord.File(data, filename))
            
      await ctx.reply(files=imgArr, embeds=embedArr, mention_author=False)

  except ai.error.InvalidRequestError as e:
    await ctx.reply("Open AI request error, please edit your request", mention_author=False)
    pass


@create.error 
async def create_error(ctx, error):
  if isinstance(error, commands.CommandError):
    await ctx.reply("You have typed the command incorrectly", mention_author=False)
      

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
         await ctx.reply("Command not found", mention_author=False)

bot.run(token)