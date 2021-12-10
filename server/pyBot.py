# import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
# .help
# ссылки на discord BOT
# https://discord.com/developers/applications :create
# https://discordpy.readthedocs.io/en/stable/ :docs
# https://discordpy.readthedocs.io/en/latest/api.html :docs
# https://discordapp.com/oauth2/authorize?client_id=ID&scope=bot&permission=8 :connect

@client.event

async def on_ready():
    print( 'BotConnected')

@client.command( pass_context = True)

async def hello ( ctx ):
    author = ctx.message.author
    await ctx.send(f'Hello {author.mention}. I am a BOT for discord')

# Connect

token = open('token.txt', 'r').readline()

client.run(token)