"""WR

This module prints world records from the KZ GlobalAPI.
"""


import discord

from discord.ext import commands
from utils import kzapi


class Wr(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def wr(self, ctx, mapname, mode, runtype):
        """!wr <map> <mode> <runtype> - Get WR for map."""
        mapname = mapname.lower()
        mode = mode.lower()
        runtype = runtype.lower()
        if not kzapi.valid_search_records(mapname, mode, runtype):
            return await ctx.send('Error: Invalid search parameters for !maptop')

        data = kzapi.get_maptop(mapname, mode, runtype)
        if not data:
            mode = mode + ' ' if mode else ''
            runtype = runtype + ' ' if runtype else ''
            return await ctx.send(f'Search for !maptop {mapname} {mode}{runtype}failed')

        player = data[0]['player_name']
        time = kzapi.convert_time(data[0]['time'])
        teleports = data[0]['teleports']
        server = data[0]['server_name']
        date = data[0]['created_on'][:10]
        runid = data[0]['id']
        info = (
            f'Map: {mapname}\n'
            f'Difficulty: {kzapi.MAPS[mapname]}\n'
            f'Mode: {mode.upper()}\n'
            f'Runtype: {runtype.upper()}'
            )

        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title='World Record',
            description=info
        )
        embed.set_thumbnail(url=f'{kzapi.MAP_IMG_URL}{mapname}.jpg')
        embed.add_field(name='Player', value=player)
        embed.add_field(name='Time', value=time)
        embed.add_field(name='Teleports', value=teleports)
        embed.add_field(name='Server', value=server)
        embed.add_field(name='Date', value=date)
        embed.add_field(name='Run ID', value=runid)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Wr(bot))
