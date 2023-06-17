import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from cogs.modules import Modules

# Load bot token from .env file
load_dotenv()

# Define intents
intents = discord.Intents.all()

# Create instance of bot
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    bot.load_extension('cogs.modules')
    bot.load_extension('cogs.dice')

# Run the bot
bot.run(os.getenv('DISCORD_BOT_TOKEN'))
