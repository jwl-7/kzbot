"""Account

This module allows players to register their Steam ID in the local database.
"""


import re

import discord

from db.dbhelper import Database
from discord.ext import commands
from utils import kzapi
from utils import steamid


class Account(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = Database()
        self.db.setup()

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def setaccount(self, ctx, steam_id):
        """!setaccount <steam_id> - Register Steam ID to use PB commands."""
        if not steamid.is_valid_steamid(steam_id):
            return await ctx.send('Error: Invalid <steam_id> for !setaccount')

        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title='Account Registration'
        )
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name='Player', value=ctx.author)
        embed.add_field(name='Steam ID', value=steam_id)

        discord_id = str(ctx.author)
        if self.db.get_account(discord_id):
            self.db.update_item(discord_id, steam_id)
        else:
            self.db.add_item(discord_id, steam_id)

        return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Account(bot))
