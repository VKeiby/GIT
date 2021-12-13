# import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

# .help
# ссылки на discord BOT
# https://discord.com/developers/applications :create
# https://discordpy.readthedocs.io/en/stable/ :docs
# https://discordpy.readthedocs.io/en/latest/api.html :docs
# https://discordapp.com/oauth2/authorize?client_id=ID&scope=bot&permission=8 :connect

@client.event
async def on_ready():
    print('BotConnected')

# Clear msg
@client.command(pass_context=True)
async def clear(ctx, amount=100):  # .clear 100msg default
    await ctx.channel.purge(limit = amount)

# Clear cmd
@client.command(pass_context=True)
async def hello(ctx, amount=1):
    await ctx.channel.purge(limit = amount)

    author = ctx.message.author
    await ctx.send(f'Hello {author.mention}.')

@client.command(pass_context=True)
async def hi(ctx):
    author = ctx.message.author
    await ctx.send(f'Hello {author.mention}. I am a BOT for discord')


# Connect
token = open('token.txt', 'r').readline()
client.run(token)
