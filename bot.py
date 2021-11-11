import discord
from discord.ext import commands


bot = commands.Bot(command_prefix = "<>", intents=discord.Intents.all(),help_command=None)

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

#Dm to all users of server
@bot.command()
async def all(ctx, *, args=None):
    if args != None:
        members = ctx.guild.members
        for member in members:
            try:
                await member.send(args)
                print("sent to: " + member.name)
            except:
                print("Couldn't send: " + member.name)
    else:
        await ctx.channel.send("You didn't provide proper a message.")
    
async def get_help_embed():
    em = discord.Embed(title="Help!", description="", color=discord.Color.purple())
    em.description += f"**{bot.command_prefix}hello** : Greets the user.\n"
    em.description += f"**{bot.command_prefix}repeat <message>** : Repeats the user message.\n"
    em.description += f"**{bot.command_prefix}dm <user_id> <message>** : Dm to a particular user.\n"
    em.description += f"**{bot.command_prefix}all <message>** : Dm to everyone on the server.\n"
    em.description += f"**{bot.command_prefix}help** : Displays this message.\n"
    em.set_footer(text="Thanks for using me!", icon_url=bot.user.avatar_url)
    return em



@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        em = await get_help_embed()
        await message.channel.send(embed=em)

    await bot.process_commands(message)

@bot.command()
async def help(ctx):
    em = await get_help_embed()
    await ctx.send(embed=em)

bot.run("<YOUR_TOKEN>")
