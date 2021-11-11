import discord
from discord.ext import commands


bot = commands.Bot(command_prefix = "&")

@bot.event
async def on_ready():
    print("Your bot is ready.")

#Hello User
@bot.command()
async def hello(ctx):
    await ctx.channel.send("Hi! " + str(ctx.author.mention))

# Repeat
@bot.command()
async def repeat(ctx, *, arg=None):
    if arg == None:
        await ctx.channel.send("You forgot to include an argument.")
    else:
        await ctx.channel.send(str(ctx.author.mention) + " " + str(arg))

#Dm to particular user
@bot.command()
async def dm(ctx, user_id=None, *, args=None):
    if user_id != None and args != None:
        try:
            target = await bot.fetch_user(user_id)
            await target.send(args)

            await ctx.channel.send("'" + args + "' sent to: " + target.name)

        except:
            await ctx.channel.send("Couldn't dm the given user.")
        

    else:
        await ctx.channel.send("You didn't provide a user's id and/or a message.")


bot.run("<YOUR_TOKEN>")
