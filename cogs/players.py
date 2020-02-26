"""Players

This module allows players to register their steamid in the local database.
"""


import re

import discord
from discord.ext import commands
from utils import kzapi

from db.dbhelper import Database


class Players(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = Database()
        self.db.setup()

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def setaccount(self, ctx, steamid):
        """!setaccount <steamid> - Register steamid to use !pb command."""
        if not re.match(r'^STEAM_([0-5]):([0-1]):([0-9]+)$', steamid):
            return await ctx.send('Error: Invalid <steamid> for !setaccount')

        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title='Account Registration'
        )
        embed.set_thumbnail(url=f'{ctx.author.avatar_url}')
        embed.add_field(name='Player', value=f'{ctx.author}')
        embed.add_field(name='Steam ID', value=f'{steamid}')

        accounts = self.db.get_items()
        for record in accounts:
            if record[0] == ctx.author:
                self.db.update_item(str(ctx.author), steamid)
                return await ctx.send(embed=embed)

        self.db.add_item(str(ctx.author), steamid)
        return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Players(bot))
