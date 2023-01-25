import discord
from discord.ext import commands

client = commands.Bot(command_prefix='e.', help_command=None, intents=discord.Intents.all(), test_guilds=[1030123727582666762])

@client.event
async def on_ready():
  print("Connected")

@client.event
async def on_member_join(member):
  role=await discord.utils.get(guild_id=member.guild.roles, id=1030123727603642429)
  channel = client.get_channel(11030123728157290616)

  embed = discord.Embed(
    title = "New member!",
    discription=f"{member.name}#{member.discriminator}",
    color=0xffffff
  )

  await member.add_roles(role)
  await channel.send(embed=embed)

client.event
async def on_command_error(ctx, error):
 print(error)

 if isinstance(error, commands.MissingPermisions):
  await ctx.send(f"{ctx.author}, у вас недостаточно прав для выполнения данной команды")
 elif isinstance(error, commands.UserInputError):
  await ctx.send(embed=discord.Embed(
    description=f"Правильное использование команды: '{ctx.prefix}{ctx.command.name}' ({ctx.command.brief})\nExample: {ctx.prefix}{ctx.command.usage}"
  ))

@client.command()
async def hello(ctx):
  await ctx.send("Hello world")

@client.command(usage="kick <@user> <reason=None>", brief="Команда для кика участника")
@commands.has_permissions(kick_members=True, administrator=True)
async def kick(ctx, member: discord.Member, *, reason = "Нарушение правил"):
  await ctx.send(f"Администратор {ctx.author.mention} исключил пользователя {member.mention}")
  await member.kick(reason = reason)
  await ctx.message.delete()

@client.command(usage="ban <@user> <reason=None>", brief="Команда для бана участника")
@commands.has_permissions(ban_members=True, administrator=True)
async def ban(ctx, member: discord.Member, *, reason = "Нарушение правил"):
  await ctx.send(f"Администратор {ctx.author.mention} забанил пользователя пользователя {member.mention}")
  await member.ban(reason = reason)
  await ctx.message.delete()

token = open('token.txt', 'r').readline()

client.run(token)