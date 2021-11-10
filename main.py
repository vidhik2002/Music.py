import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix=";-;", intents = discord.Intents.all())
client.run(os.getenv("TOKEN"))


