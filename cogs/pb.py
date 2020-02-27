"""Pb

This module prints personal best times from the KZ GlobalAPI.
"""


import discord

from db.dbhelper import Database
from discord.ext import commands
from utils import kzapi


class Pb(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = Database()

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def pb(self, ctx, mapname, mode='kzt', runtype='pro'):
        """!pb <map> <mode> <runtype> - Get personal best time for map."""
        discord_id = str(ctx.author)
        account = self.db.get_account(discord_id)
        if not account:
            return await ctx.send(
                'Error: You need to register your Steam ID with !setaccount <steam_id>'
            )

        steam_id = account[1]
        mapname = mapname.lower()
        mode = mode.lower()
        runtype = runtype.lower()
        if not kzapi.valid_search_records(mapname, mode, runtype):
            return await ctx.send('Error: Invalid search parameters for !pb')

        data = kzapi.get_pb(steam_id, mapname, mode, runtype)
        if not data:
            return await ctx.send(f'Search for !pb {mapname} {mode} {runtype} failed')

        player = data[0]['player_name']
        mode = kzapi.MODES_ALT[data[0]['mode']]
        time = kzapi.convert_time(data[0]['time'])
        teleports = data[0]['teleports']
        server = data[0]['server_name']
        date = data[0]['created_on'][:10]

        info = (
            f'Map: {mapname}\n'
            f'Difficulty: {kzapi.MAPS[mapname]}\n'
            f"Mode: {mode.upper()}\n"
            f"Runtype: {runtype.upper()}"
            )

        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title='Personal Best',
            description=info
        )
        embed.set_thumbnail(url=f'{kzapi.MAP_IMG_URL}{mapname}.jpg')
        embed.add_field(name='Player', value=player)
        embed.add_field(name='Time', value=time)
        embed.add_field(name='Teleports', value=teleports)
        embed.add_field(name='Server', value=server)
        embed.add_field(name='Date', value=date)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Pb(bot))
