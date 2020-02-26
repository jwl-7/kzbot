"""Recent

This module prints recent world records and bans from the KZ GlobalAPI.
"""


import discord

from discord.ext import commands
from utils import kzapi


class Recent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['latest', 'latestwrs'])
    @commands.cooldown(1, 10, commands.BucketType.channel)
    async def recentwrs(self, ctx):
        """!recentwrs - Get recent WRs."""
        data = kzapi.get_recent_wrs()
        if not data:
            return await ctx.send('Search for !recentwrs failed')

        players = ''
        maps = ''
        times = ''
        for x in range(len(data)):
            mode = kzapi.MODES_ALT[data[x]['mode']].upper()
            runtype = 'TP' if data[x]['teleports'] else 'PRO'
            players += f"{data[x]['player_name']}\n"
            maps += f"{data[x]['map_name']}\n"
            times += f"({mode}/{runtype}) {kzapi.convert_time(data[x]['time'])}\n"

        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title='Recent World Records'
        )
        embed.add_field(name='Player', value=players)
        embed.add_field(name='Map', value=maps)
        embed.add_field(name='Time', value=times)
        await ctx.send(embed=embed)

    @commands.command(aliases=['latestbans'])
    @commands.cooldown(1, 10, commands.BucketType.channel)
    async def recentbans(self, ctx):
        """!recentbans - Get recent bans."""
        data = kzapi.get_recent_bans()
        if not data:
            return await ctx.send('Search for !recentbans failed')

        players = ''
        ban_types = ''
        dates = ''
        for x in range(len(data)):
            players += f"{data[x]['player_name']}\n"
            ban_types += f"{data[x]['ban_type']}\n"
            dates += f"{data[x]['created_on'][:10]}\n"

        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title='Recent Global Bans'
        )
        embed.add_field(name='Player', value=players)
        embed.add_field(name='Reason', value=ban_types)
        embed.add_field(name='Date', value=dates)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Recent(bot))
