"""JumpPb

This module prints personal best jumpstats from the KZ GlobalAPI.
"""


import discord

from db.dbhelper import Database
from discord.ext import commands
from utils import kzapi


class JumpPb(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = Database()

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def jumppb(self, ctx, bindtype='nobind'):
        """!jumppb <bind/nobind> - Get personal best jumpstats."""
        discord_id = str(ctx.author)
        account = self.db.get_account(discord_id)
        if not account:
            return await ctx.send(
                'Error: You need to register your Steam ID with !setaccount <steam_id>'
            )

        bindtype = bindtype.lower()
        if not kzapi.valid_search_jumppb(bindtype):
            return await ctx.send('Error: Invalid search parameters for !jumppb')

        steam_id = account[1]
        jumptypes = ''
        distances = ''
        strafes = ''
        for jumptype in kzapi.JUMPTYPES_ALT:
            data = kzapi.get_jumppb(steam_id, jumptype, bindtype)
            jumptypes += f'{jumptype}\n'
            distances += f"{data[0]['distance']}\n" if data else 'N/A\n'
            strafes += f"{data[0]['strafe_count']}\n" if data else 'N/A\n'

        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title=f'Personal Best Jumpstats',
            description=f"Type: {'No Bind' if bindtype == 'nobind' else 'Binded'}"
        )
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name='Player', value=ctx.author.name, inline=False)
        embed.add_field(name='Jumptype', value=jumptypes)
        embed.add_field(name='Distance', value=distances)
        embed.add_field(name='Strafes', value=strafes)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(JumpPb(bot))
