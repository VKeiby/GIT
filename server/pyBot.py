import discord
from discord.ext import commands

PREFX = '.'
client = commands.Bot(command_prefix=PREFX)
client.remove_command('help')

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
@commands.has_permissions(administrator = True)
async def clear(ctx, amount=100):  # .clear 100msg default
    await ctx.channel.purge(limit = amount)


# Clear cmd
@client.command(pass_context=True)
async def hello(ctx, amount=1):
    await ctx.channel.purge(limit = amount+1)

    author = ctx.message.author
    await ctx.send(f'Hello {author.mention}.')

@client.command(pass_context=True)
async def hi(ctx):
    author = ctx.message.author
    await ctx.send(f'Hello {author.mention}. I am a BOT for discord')

# Kick
@client.command(pass_context=True)
@commands.has_permissions(administrator = True)

async def kick(ctx, member: discord.Member, *, reason = None):
    await ctx.channel.purge( limit =1)

    await member.kick( reason=reason)
    await ctx.send(f'User { member.mention} was kicked by admin')


# Ban
@client.command(pass_content= True)
@commands.has_permissions(administrator = True)

async def ban(ctx, member: discord.Member, *, reason = None):
    await ctx.channel.purge( limit =1)

    await member.ban( reason=reason)
    await ctx.send(f'User { member.mention} was banned by admin for {reason}')


# Unban
@client.command(pass_content= True)
@commands.has_permissions(administrator = True)

async def unban(ctx, *, member):
    await ctx.channel.purge( limit =1)

    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user

        await ctx.guild.unban( user )
        await ctx.send (f'User { user.mention} was unbanned')

        return

# HELP Command
@client.command(pass_content= True)
# @commands.has_permissions(administrator = True)

async def help(ctx):
    emb = discord.Embed(title = 'Commands:')

    emb.add_field(name = '{}clear'.format(PREFX), value = 'Clear chats')
    emb.add_field(name = '{}kick'.format(PREFX), value = 'Kick member')
    emb.add_field(name = '{}ban'.format(PREFX), value = 'Ban member')
    emb.add_field(name = '{}hello'.format(PREFX), value = 'Say Hello')
    emb.add_field(name = '{}help'.format(PREFX), value = 'This message')
    emb.add_field(name = '{}unban'.format(PREFX), value = 'Unban member')

    await ctx.send( embed = emb)



# Connect
token = open('token.txt', 'r').readline()
client.run(token)
