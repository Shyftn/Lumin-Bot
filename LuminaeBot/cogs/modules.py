import discord
from discord.ext import commands
import random

class Modules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='roll', help='Rolls a dice in NdN format.')
    async def roll(self, ctx, dice: str):
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    @commands.command(name='create-character', help='Creates a new character.')
    async def create_character(self, ctx, character_name: str):
        await ctx.send(f'Character "{character_name}" created!')

    @commands.command(name='delete-character', help='Deletes a specified character.')
    async def delete_character(self, ctx, character_name: str):
        await ctx.send(f'Character "{character_name}" deleted!')

    @commands.command(name='update-character', help='Updates a specified character.')
    async def update_character(self, ctx, character_name: str):
        await ctx.send(f'Character "{character_name}" updated!')

def setup(bot):
    bot.add_cog(Modules(bot))
