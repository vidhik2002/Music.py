
import asyncio
import youtube_dl
import pafy
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="<>", intents=intents,help_command=None)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready.")

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

#Emoji
@bot.command()
async def emoji(ctx,*, arg=None):
    try:
        if arg == "catdrink":
            embed = discord.Embed()
            embed.set_image(url="https://emoji.gg/assets/emoji/1218-blobcatdrink.png")
            await ctx.channel.send(embed=embed)
        if arg == "cookie":
            embed = discord.Embed()
            embed.set_image(url="https://emoji.gg/assets/emoji/7307-blobcookie.png")
            await ctx.channel.send(embed=embed)
        if arg == "flushed":
            embed = discord.Embed()
            embed.set_image(url="https://emoji.gg/assets/emoji/6471-blobflushed.png")
            await ctx.channel.send(embed=embed)
        if arg == "gun":
            embed = discord.Embed()
            embed.set_image(url="https://emoji.gg/assets/emoji/1619-blobgun.png")
            await ctx.channel.send(embed=embed)
        if arg == "axe":
            embed = discord.Embed()
            embed.set_image(url="https://emoji.gg/assets/emoji/5005-blob-diamond-axe.png")
            await ctx.channel.send(embed=embed)
        if arg == "pat":
            embed = discord.Embed()
            embed.set_image(url="https://emoji.gg/assets/emoji/5289-blobpensivepat.gif")
            await ctx.channel.send(embed=embed)
        if arg == "cry":
            embed = discord.Embed()
            embed.set_image(url="https://emoji.gg/assets/emoji/2936-crycat2.png")
            await ctx.channel.send(embed=embed)
        if arg == "shutup":
            embed = discord.Embed()
            embed.set_image(url="https://emoji.gg/assets/emoji/1108-vibing.gif")
            await ctx.channel.send(embed=embed)
        if arg == "scared":
            embed = discord.Embed()
            embed.set_image(url="https://emoji.gg/assets/emoji/3613-pepe-with-jesus.png")
            await ctx.channel.send(embed=embed)
        if arg == "party":
            embed = discord.Embed()
            embed.set_image(url="https://emoji.gg/assets/emoji/9056-peped.gif")
            await ctx.channel.send(embed=embed)
        if arg == "fu":
            embed = discord.Embed()
            embed.set_image(url="https://emoji.gg/assets/emoji/8399-pepe-fuck-you.png")
            await ctx.channel.send(embed=embed)
    except:
        await ctx.channel.send("You forgot to include a valid argument.")
#Snipe
bot.sniped_messages = {}

@bot.event
async def on_message_delete(message):
    bot.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)

@bot.command()
async def snipe(ctx):
    try:
        contents, author, channel_name, time = bot.sniped_messages[ctx.guild.id]
        
    except:
        await ctx.channel.send("Couldn't find a message to snipe!")
        return

    embed = discord.Embed(description=contents, color=discord.Color.purple(), timestamp=time)
    embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
    embed.set_footer(text=f"Deleted in : #{channel_name}")

    await ctx.channel.send(embed=embed)

#Dm a user
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

#Help command    
async def get_help_embed():
    em = discord.Embed(title="Help!", description="", color=discord.Color.purple())
    em.description += f"**{bot.command_prefix}hello** : Greets the user.\n"
    em.description += f"**{bot.command_prefix}repeat <message>** : Repeats the user message.\n"
    em.description += f"**{bot.command_prefix}dm <user_id> <message>** : Dm to a particular user.\n"
    em.description += f"**{bot.command_prefix}all <message>** : Dm to everyone on the server.\n"
    em.description += f"**{bot.command_prefix}help** : Displays this message.\n"
    em.description += f"**{bot.command_prefix}join** : joins the voice channel.\n"
    em.description += f"**{bot.command_prefix}play <song>** : Plays the desired song.\n"
    em.description += f"**{bot.command_prefix}search <song>** : Searches for songs.\n"
    em.description += f"**{bot.command_prefix}queue** : Shows the queue.\n"
    em.description += f"**{bot.command_prefix}skip** : Skips the current song on vote.\n"
    em.description += f"**{bot.command_prefix}pause** : Pauses the current song.\n"
    em.description += f"**{bot.command_prefix}resume** : Resumes the current song.\n"
    em.description += f"**{bot.command_prefix}leave** : Leaves the voice channel.\n"
    em.description += f"**{bot.command_prefix}emoji <emoji_args>** : Displays emojis.\n"
    em.add_field(name="<emoji_args>", value="catdrink, cookie, flushed, gun, axe, pat, cry, shutup, scared, party, fu", inline=True)
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

#Music Bot    
class Player(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        self.song_queue = {}

        self.setup()

    def setup(self):
        for guild in self.bot.guilds:
            self.song_queue[guild.id] = []

    async def check_queue(self, ctx):
        if len(self.song_queue[ctx.guild.id]) > 0:
            await self.play_song(ctx, self.song_queue[ctx.guild.id][0])
            self.song_queue[ctx.guild.id].pop(0)

    async def search_song(self, amount, song, get_url=False):
        info = await self.bot.loop.run_in_executor(None, lambda: youtube_dl.YoutubeDL({"format" : "bestaudio", "quiet" : True}).extract_info(f"ytsearch{amount}:{song}", download=False, ie_key="YoutubeSearch"))
        if len(info["entries"]) == 0: return None

        return [entry["webpage_url"] for entry in info["entries"]] if get_url else info

    async def play_song(self, ctx, song):
        url = pafy.new(song).getbestaudio().url
        ctx.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url)), after=lambda error: self.bot.loop.create_task(self.check_queue(ctx)))
        ctx.voice_client.source.volume = 0.5

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            return await ctx.send("You are not connected to a voice channel, please connect to the channel you want the bot to join.")

        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()

        await ctx.author.voice.channel.connect()

    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client is not None:
            return await ctx.voice_client.disconnect()

        await ctx.send("I am not connected to a voice channel.")

    @commands.command()
    async def play(self, ctx, *, song=None):
        if song is None:
            return await ctx.send("You must include a song to play.")

        if ctx.voice_client is None:
            return await ctx.send("I must be in a voice channel to play a song.")

        # handle song where song isn't url
        if not ("youtube.com/watch?" in song or "https://youtu.be/" in song):
            await ctx.send("Searching for song, this may take a few seconds.")

            result = await self.search_song(1, song, get_url=True)

            if result is None:
                return await ctx.send("Sorry, I could not find the given song, try using my search command.")

            song = result[0]

        if ctx.voice_client.source is not None:
            queue_len = len(self.song_queue[ctx.guild.id])

            if queue_len < 10:
                self.song_queue[ctx.guild.id].append(song)
                return await ctx.send(f"I am currently playing a song, this song has been added to the queue at position: {queue_len+1}.")

            else:
                return await ctx.send("Sorry, I can only queue up to 10 songs, please wait for the current song to finish.")

        await self.play_song(ctx, song)
        await ctx.send(f"Now playing: {song}")

    @commands.command()
    async def search(self, ctx, *, song=None):
        if song is None: return await ctx.send("You forgot to include a song to search for.")

        await ctx.send("Searching for song, this may take a few seconds.")

        info = await self.search_song(5, song)

        embed = discord.Embed(title=f"Results for '{song}':", description="*You can use these URL's to play an exact song if the one you want isn't the first result.*\n", colour=discord.Colour.red())
        
        amount = 0
        for entry in info["entries"]:
            embed.description += f"[{entry['title']}]({entry['webpage_url']})\n"
            amount += 1

        embed.set_footer(text=f"Displaying the first {amount} results.")
        await ctx.send(embed=embed)

    @commands.command()
    async def queue(self, ctx): # display the current guilds queue
        if len(self.song_queue[ctx.guild.id]) == 0:
            return await ctx.send("There are currently no songs in the queue.")

        embed = discord.Embed(title="Song Queue", description="", colour=discord.Colour.dark_gold())
        i = 1
        for url in self.song_queue[ctx.guild.id]:
            embed.description += f"{i}) {url}\n"

            i += 1

        embed.set_footer(text="Thanks for using me!")
        await ctx.send(embed=embed)

    @commands.command()
    async def skip(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send("I am not playing any song.")

        if ctx.author.voice is None:
            return await ctx.send("You are not connected to any voice channel.")

        if ctx.author.voice.channel.id != ctx.voice_client.channel.id:
            return await ctx.send("I am not currently playing any songs for you.")

        poll = discord.Embed(title=f"Vote to Skip Song by - {ctx.author.name}#{ctx.author.discriminator}", description="**80% of the voice channel must vote to skip for it to pass.**", colour=discord.Colour.blue())
        poll.add_field(name="Skip", value=":white_check_mark:")
        poll.add_field(name="Stay", value=":no_entry_sign:")
        poll.set_footer(text="Voting ends in 10 seconds.")

        poll_msg = await ctx.send(embed=poll) # only returns temporary message, we need to get the cached message to get the reactions
        poll_id = poll_msg.id

        await poll_msg.add_reaction(u"\u2705") # yes
        await poll_msg.add_reaction(u"\U0001F6AB") # no
        
        await asyncio.sleep(10) # 10 seconds to vote

        poll_msg = await ctx.channel.fetch_message(poll_id)
        
        votes = {u"\u2705": 0, u"\U0001F6AB": 0}
        reacted = []

        for reaction in poll_msg.reactions:
            if reaction.emoji in [u"\u2705", u"\U0001F6AB"]:
                async for user in reaction.users():
                    if user.voice.channel.id == ctx.voice_client.channel.id and user.id not in reacted and not user.bot:
                        votes[reaction.emoji] += 1

                        reacted.append(user.id)

        skip = False

        if votes[u"\u2705"] > 0:
            if votes[u"\U0001F6AB"] == 0 or votes[u"\u2705"] / (votes[u"\u2705"] + votes[u"\U0001F6AB"]) > 0.79: # 80% or higher
                skip = True
                embed = discord.Embed(title="Skip Successful", description="***Voting to skip the current song was succesful, skipping now.***", colour=discord.Colour.green())

        if not skip:
            embed = discord.Embed(title="Skip Failed", description="*Voting to skip the current song has failed.*\n\n**Voting failed, the vote requires at least 80% of the members to skip.**", colour=discord.Colour.red())

        embed.set_footer(text="Voting has ended.")

        await poll_msg.clear_reactions()
        await poll_msg.edit(embed=embed)

        if skip:
            ctx.voice_client.stop()


    @commands.command()
    async def pause(self, ctx):
        if ctx.voice_client.is_paused():
            return await ctx.send("I am already paused.")

        ctx.voice_client.pause()
        await ctx.send("The current song has been paused.")

    @commands.command()
    async def resume(self, ctx):
        if ctx.voice_client is None:
            return await ctx.send("I am not connected to a voice channel.")

        if not ctx.voice_client.is_paused():
            return await ctx.send("I am already playing a song.")
        
        ctx.voice_client.resume()
        await ctx.send("The current song has been resumed.")

async def setup():
    await bot.wait_until_ready()
    bot.add_cog(Player(bot))

bot.loop.create_task(setup())

bot.run("<YOUR_TOKEN>")

