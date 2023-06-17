import discord
from discord.ext import commands
import random

class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='roll', help='Rolls a dice in NdN format.')
    async def roll(self, ctx, dice: str):
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return

        if rolls > 100:
            await ctx.send('I can\'t roll that many dice. Please try a number less than 100.')
            return

        if limit > 100:
            await ctx.send('I can\'t roll a dice with that many sides. Please try a number less than 100.')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))

        await ctx.send(result)

    @commands.command(name='roll_advantage', help='Rolls two d20s and takes the higher result.')
    async def roll_advantage(self, ctx):
        result = max(random.randint(1, 20), random.randint(1, 20))
        await ctx.send(result)

    @commands.command(name='roll_disadvantage', help='Rolls two d20s and takes the lower result.')
    async def roll_disadvantage(self, ctx):
        result = min(random.randint(1, 20), random.randint(1, 20))
        await ctx.send(result)

def setup(bot):
    bot.add_cog(Dice(bot))
