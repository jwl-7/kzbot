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
    async def jumptop(self, ctx, jumptype):
        """!jumptop <jumptype> - Get top jumpstats."""
        jumptype = jumptype.lower()
        if not kzapi.valid_search_jumpstats(jumptype):
            return await ctx.send('Error: Invalid search parameters for !jumptop')

        if jumptype in kzapi.JUMPTYPES:
            jumptype = kzapi.JUMPTYPES[jumptype]

        data = kzapi.get_jumptop(jumptype)
        if not data:
            jumptype = jumptype + ' ' if jumptype else ''
            return await ctx.send(f'Search for !jumptop {jumptype}failed')

        positions = ''
        players = ''
        distances = ''
        for x in range(len(data)):
            positions += f'{x + 1}\n'
            players += f"{data[x]['player_name']}\n"
            distances += f"{data[x]['distance']}\n"
        info = (
            'Mode: No Bind\n'
            f'Jumptype: {jumptype.capitalize()}'
            )

        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title=f'Top Jumpstats',
            description=info
        )
        embed.add_field(name='#', value=positions)
        embed.add_field(name='Player', value=players)
        embed.add_field(name='Distance', value=distances)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Jumpstats(bot))
