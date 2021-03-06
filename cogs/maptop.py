"""Maptop

This module prints top map times from the KZ GlobalAPI.
"""


import discord

from discord.ext import commands
from utils import kzapi


class Maptop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def maptop(self, ctx, mapname, mode='kzt', runtype='pro'):
        """!maptop <map> <mode> <runtype> - Get top times for map."""
        embed = discord.Embed(colour=discord.Colour.darker_grey())
        mapname = mapname.lower()
        mode = mode.lower()
        runtype = runtype.lower()
        if not kzapi.valid_search_records(mapname, mode, runtype):
            embed.description = 'Invalid search parameters for **!maptop**'
            return await ctx.send(embed=embed)

        data = kzapi.get_maptop(mapname, mode, runtype)
        if not data:
            embed.description = f'Search for **!maptop** *{mapname} {mode} {runtype}* failed.'
            return await ctx.send(embed=embed)

        players = ''
        times = ''
        teleports = ''
        for x in range(len(data)):
            players += f"{data[x]['player_name']}\n"
            times += f"{kzapi.convert_time(data[x]['time'])}\n"
            teleports += f"{data[x]['teleports']}\n"

        info = (
            f'Map: {mapname}\n'
            f'Difficulty: {kzapi.MAPS[mapname]}\n'
            f"Mode: {mode.upper()}\n"
            f"Runtype: {runtype.upper()}"
            )

        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title='Map Top',
            description=info
        )
        embed.set_thumbnail(url=f'{kzapi.MAP_IMG_URL}{mapname}.jpg')
        embed.add_field(name='Player', value=players)
        embed.add_field(name='Time', value=times)
        embed.add_field(name='Teleports', value=teleports)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Maptop(bot))
