import discord
from discord.ext import commands


bot = commands.Bot(command_prefix = "&")

@bot.event
async def on_ready():
    print("Your bot is ready.")

@bot.command()
async def hello(ctx):
    await ctx.channel.send("Hi! " + str(ctx.author.mention))

@bot.command()
async def repeat(ctx, *, arg=None):
    if arg == None:
        await ctx.channel.send("You forgot to include an argument.")
    else:
        await ctx.channel.send(str(ctx.author.mention) + " " + str(arg))

bot.run("<YOUR_TOKEN>")
