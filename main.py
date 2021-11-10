import discord
from discord.ext import commands
import os
TOKEN = os.getenv("TOKEN")

client = commands.Bot(command_prefix=";-;", intents = discord.Intents.all())
client.run(TOKEN)

print(TOKEN)



