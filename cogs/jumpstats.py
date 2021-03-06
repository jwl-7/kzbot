"""Jumpstats

This module prints top jumpstats from the KZ GlobalAPI.
"""


import discord

from discord.ext import commands
from utils import kzapi


class Jumpstats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def jumptop(self, ctx, jumptype, bindtype='nobind'):
        """!jumptop <jumptype> <bind/nobind> - Get top jumpstats."""
        embed = discord.Embed(colour=discord.Colour.darker_grey())
        jumptype = jumptype.lower()
        bindtype = bindtype.lower()
        if not kzapi.valid_search_jumpstats(jumptype, bindtype):
            embed.description = 'Invalid search parameters for **!jumptop**'
            return await ctx.send(embed=embed)

        if jumptype in kzapi.JUMPTYPES:
            jumptype = kzapi.JUMPTYPES[jumptype]

        data = kzapi.get_jumptop(jumptype, bindtype)
        if not data:
            embed.description = f'Search for **!jumptop** *{jumptype} {bindtype}* failed.'
            return await ctx.send(embed=embed)

        positions = ''
        players = ''
        distances = ''
        for x in range(len(data)):
            positions += f'{x + 1}\n'
            players += f"{data[x]['player_name']}\n"
            distances += f"{data[x]['distance']}\n"

        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title=f'Top Jumpstats',
            description=f"Type: {'No Bind' if bindtype == 'nobind' else 'Binded'}"
        )
        embed.add_field(name='#', value=positions)
        embed.add_field(name='Player', value=players)
        embed.add_field(name='Distance', value=distances)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Jumpstats(bot))
