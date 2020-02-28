"""Help

This module contains help commands.
"""


import discord

from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.channel)
    async def kzbothelp(self, ctx):
        """!kzbothelp - DM KZBOT command list."""
        info_cmds = (
            '**!apistatus** - Check KZ Global API status.\n'
            '**!kzbothelp** - DM KZBOT command list.\n'
            '**!kzbotstatus** - KZBOT stats.\n'
            '**!ping** - Test BOT latency.'
            )
        record_cmds = (
            '**!jumptop** *<jumptype> <bind/nobind>* - Get top jumpstats.\n'
            '**!maptop** *<map> <mode> <runtype>* - Get top times for map.\n'
            '**!recentbans** - Get recent bans.\n'
            '**!recentwrs** - Get recent WRs.\n'
            '**!wr** *<map> <mode> <runtype>* - Get WR for map.'
            )
        leaderboard_cmds = (
            '**!top** *<mode> <runtype>* - Get top players on records leaderboard.\n'
            '**!ranktop** *<mode> <runtype>* - Get top players on points leaderboard.'
            )
        pb_cmds = (
            '**!jumppb** *<bind/nobind>* - Get personal best jumpstats.\n'
            '**!pb** *<map> <mode> <runtype>* - Get personal best time for map.\n'
            '**!rank** *<mode> <runtype>* - Get personal rank on points leaderboard.\n'
            '**!setaccount** *<steam_id>* - Register Steam ID to use PB commands.'
            )

        embed = discord.Embed(
            colour=discord.Colour.green(),
            title='KZBOT - Command List'
        )
        embed.add_field(name='Info Commands', value=info_cmds, inline=False)
        embed.add_field(name='Record Commands', value=record_cmds, inline=False)
        embed.add_field(name='Leaderboard Commands', value=leaderboard_cmds, inline=False)
        embed.add_field(name='Personal Best Commands', value=pb_cmds, inline=False)
        await ctx.author.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def adminhelp(self, ctx):
        """!adminhelp - DM KZBOT admin command list."""
        admin_cmds = (
            '**!adminhelp** - DM KZBOT admin command list.\n'
            '**!load** *<name>* - Load extension.\n'
            '**!unload** *<name>* - Unload extension.\n'
            '**!reload** *<name>* - Reload extension.\n'
            '**!restart** - Restart KZBOT.'
            )

        embed = discord.Embed(
            colour=discord.Colour.red(),
            title='KZBOT - Admin Command List'
        )
        embed.add_field(name=admin_cmds, value='\u200b')
        await ctx.author.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
