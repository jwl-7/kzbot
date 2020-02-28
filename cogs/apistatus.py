"""KZ

This module fetches the status of the KZ GlobalAPI.
"""


import discord

from bs4 import BeautifulSoup
from discord.ext import commands
from utils import kzapi


class ApiStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def apistatus(self, ctx):
        """!apistatus - Check KZ GlobalAPI status."""
        html_page = kzapi.get_status()
        if not html_page:
            embed = discord.Embed(colour=discord.Colour.darker_grey())
            embed.description = 'Failed to retrieve GlobalAPI status.'
            return await ctx.send(embed=embed)

        soup = BeautifulSoup(html_page, 'html.parser')
        status = soup.find('span', class_='status').get_text(strip=True)
        uptime_data = soup.find_all('div', class_='legend-item-uptime-value')
        uptime_percents = []
        for x in range(len(uptime_data)):
            num = uptime_data[x].find('span').get_text(strip=True)
            uptime_percents.append(f'{num}%')

        uptimes = (
            f'GlobalAPI.com - {uptime_percents[0]}\n'
            f'GlobalAPI Portal - {uptime_percents[1]}\n'
            f'GlobalAPI Backend - {uptime_percents[2]}\n'
            f'KZStats.com - {uptime_percents[3]}\n'
            f'KZTimer Global Database - {uptime_percents[4]}'
            )

        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title=f'KZ GlobalAPI'
        )
        embed.set_thumbnail(url='https://i.imgur.com/sSqZw6W.png')
        embed.add_field(name='GlobalAPI Status', value=status, inline=False)
        embed.add_field(name='Uptime over past 90 days', value=uptimes, inline=False)
        embed.add_field(name='Status Page', value=kzapi.GAPI_STATUS_URL, inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ApiStatus(bot))
