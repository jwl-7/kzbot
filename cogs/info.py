"""Info

This module contains help commands.
"""


import os
import time

import discord
import psutil

from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            self.bot.messages_sent += 1
        self.bot.message_count += 1

        if (
            self.bot.user.name.lower() in message.content.lower() or
            self.bot.user.mentioned_in(message)
        ):
            self.bot.mentions_count += 1

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.channel)
    async def kzbothelp(self, ctx):
        """!kzbothelp - DM bot command list."""
        info_cmds = (
            '**!apistatus** - Get KZ Global API status.\n'
            '**!kzbothelp** - DM BOT command list.\n'
            '**!kzbotstatus** - Get KZBOT stats.\n'
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
            '**!rank** *<mode>* - Get personal rank on points leaderboard.\n'
            '**!setaccount** *<steam_id>* - Register Steam ID to use !pb command.'
            )
        embed = discord.Embed(colour=discord.Colour.green())
        embed.set_author(
            name='KZ BOT - Command List',
            icon_url='https://i.imgur.com/sSqZw6W.png'
        )
        embed.add_field(name='Info Commands', value=info_cmds, inline=False)
        embed.add_field(name='Record Commands', value=record_cmds, inline=False)
        embed.add_field(name='Leaderboard Commands', value=leaderboard_cmds, inline=False)
        embed.add_field(name='Personal Best Commands', value=pb_cmds, inline=False)
        try:
            await ctx.author.send(embed=embed)
        except discord.Forbidden:
            return print(f'[ERROR] Failed to send !help list to {ctx.author.name}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def adminhelp(self, ctx):
        """!adminhelp - DM bot admin command list."""
        admin_cmds = (
            '**!adminhelp** - DM BOT admin command list.\n'
            '**!load** *<name>* - Load extension.\n'
            '**!unload** *<name>* - Unload extension.\n'
            '**!reload** *<name>* - Reload extension.\n'
            '**!restart** - Restart BOT.'
            )

        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_author(
            name='KZ BOT - Admin Command List',
            icon_url='https://i.imgur.com/sSqZw6W.png'
        )
        embed.add_field(name=admin_cmds, value='\u200b')
        try:
            await ctx.author.send(embed=embed)
        except discord.Forbidden:
            return print(f'[ERROR] Failed to send !adminhelp list to {ctx.author.name}')

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.channel)
    async def ping(self, ctx):
        """!ping - Test bot latency."""
        latency = self.bot.latency
        milliseconds = int(round(latency * 1000))

        embed = discord.Embed(colour=discord.Colour.green())
        embed.add_field(name='Pong!', value=f'Latency: *{milliseconds}ms*')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.channel)
    async def kzbotstatus(self, ctx):
        """!kzbotstatus - Get stats on kzbot."""
        uptime = time.time() - self.bot.uptime
        minutes, seconds = divmod(uptime, 60)
        hours, minutes = divmod(minutes, 60)

        process = psutil.Process(os.getpid())
        mem_usage = process.memory_info().rss
        mem_usage /= 1024 ** 2

        embed = discord.Embed(colour=discord.Colour.green())
        embed.set_author(
            name='KZ BOT - Status',
            icon_url='https://i.imgur.com/sSqZw6W.png'
        )
        embed.add_field(
            name='🕖 Uptime',
            value=f'{int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds',
            inline=False
        )
        embed.add_field(name='📥 Messages Received', value=self.bot.message_count)
        embed.add_field(name='📤 Messages Sent', value=self.bot.messages_sent)
        embed.add_field(name='🏷️ Mentions', value=self.bot.mentions_count)
        embed.add_field(name='💾 Memory Usage', value=f'{mem_usage:.2f} MiB')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
