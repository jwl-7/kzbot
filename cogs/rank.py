"""Rank

This module prints world records from the KZ GlobalAPI.
"""


import discord

from db.dbhelper import Database
from discord.ext import commands
from utils import kzapi
from utils import steamid


class Rank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = Database()

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def rank(self, ctx, mode, runtype='pro'):
        """!rank <mode> - Get personal rank on points leaderboard."""
        discord_id = str(ctx.author)
        account = self.db.get_account(discord_id)
        if not account:
            return await ctx.send(
                'Error: You need to register your Steam ID with !setaccount <steam_id>'
            )

        mode = mode.lower()
        if not kzapi.valid_search_leaderboard(mode, runtype):
            return await ctx.send('Error: Invalid search parameters for !rank')

        steam_id = account[1]
        steam64 = steamid.steamid_to_steam64(steam_id)
        data = kzapi.get_rank(steam64, mode, runtype)
        if not data:
            return await ctx.send(f'Search for !rank {mode} {runtype} failed')

        player = data[0]['player_name']
        points = data[0]['points']
        average = data[0]['average']
        finishes = data[0]['finishes']
        info = (
            f'Mode: {mode.upper()}\n'
            f'Runtype: {runtype.upper()}'
            )

        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title='Rank',
            description=info
        )
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name='Player', value=player, inline=False)
        embed.add_field(name='Points', value=points)
        embed.add_field(name='Average', value=average)
        embed.add_field(name='Map Completions', value=finishes)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Rank(bot))
