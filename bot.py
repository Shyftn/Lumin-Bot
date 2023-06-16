import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from cogs.modules import Modules

# Load bot token from .env file
load_dotenv()
bot_token = os.getenv('DISCORD_BOT_TOKEN')

# Define intents
intents = discord.Intents.default()

# Create instance of bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Add Modules cog to the bot
bot.add_cog(Modules(bot))

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    bot.load_extension('cogs.dice')  # Add this line to load the Dice cog
    
# Run the bot
bot.run(bot_token)
