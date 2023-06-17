import discord
from discord.ext import commands

class TTRPG(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ttrpg_command(self, ctx):
        await ctx.send('TTRPG command has been executed.')

def setup(bot):
    bot.add_cog(TTRPG(bot))
