"""Leaderboard

This module prints top players from the KZ GlobalAPI.
"""


import discord

from discord.ext import commands
from utils import kzapi


class Leaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['top10', 'leaderboard'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def top(self, ctx, mode):
        """!top <mode> - Get top players on records leaderboard."""
        mode = mode.lower()
        if not kzapi.valid_search_leaderboard(mode):
            return await ctx.send('Error: Invalid search parameters for !top')

        data = kzapi.get_wrtop(mode)
        if not data:
            mode = mode + ' ' if mode else ''
            return await ctx.send(f'Search for !top {mode}failed')

        positions = ''
        players = ''
        records = ''
        for x in range(len(data)):
            positions += f'{x + 1}\n'
            players += f"{data[x]['player_name']}\n"
            records += f"{data[x]['count']}\n"
        info = (
            f'Mode: {mode.upper()}\n'
            'Runtype: PRO'
            )

        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title='Records Leaderboard',
            description=info
        )
        embed.add_field(name='#', value=positions)
        embed.add_field(name='Player', value=players)
        embed.add_field(name='Records', value=records)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def ranktop(self, ctx, mode):
        """!ranktop <mode> - Get top players on points leaderboard."""
        mode = mode.lower()
        if not kzapi.valid_search_leaderboard(mode):
            return await ctx.send('Error: Invalid search parameters for !ranktop')

        data = kzapi.get_ranktop(mode)
        if not data:
            mode = mode + ' ' if mode else ''
            return await ctx.send(f'Search for !ranktop {mode}failed')

        positions = ''
        players = ''
        points = ''
        for x in range(len(data)):
            positions += f'{x + 1}\n'
            players += f"{data[x]['player_name']}\n"
            points += f"{data[x]['points']}\n"
        info = (
            f'Mode: {mode.upper()}\n'
            'Runtype: PRO'
            )

        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title='Points Leaderboard',
            description=info
        )
        embed.add_field(name='#', value=positions)
        embed.add_field(name='Player', value=players)
        embed.add_field(name='Points', value=points)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Leaderboard(bot))
