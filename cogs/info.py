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
            '**!apistatus** - check global api status\n'
            '**!kzbothelp** - dm bot command list\n'
            '**!kzbotstatus** - kz bot stats\n'
            '**!ping** - test bot latency'
            )
        kz_cmds = (
            '**!maptop** *<map> <kzt/skz/vnl> <pro/tp>*\n'
            '**!recentbans**\n'
            '**!recentwrs**\n'
            '**!wr** *<map> <kzt/skz/vnl> <pro/tp>*'
            )
        embed = discord.Embed(colour=discord.Colour.green())
        embed.set_author(
            name='KZ BOT - Command List',
            icon_url='https://i.imgur.com/sSqZw6W.png'
        )
        embed.add_field(name='Info', value=info_cmds, inline=False)
        embed.add_field(name='KZ Records', value=kz_cmds, inline=False)
        try:
            await ctx.author.send(embed=embed)
        except discord.Forbidden:
            return print(f'[ERROR] Failed to send !help list to {ctx.author.name}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def adminhelp(self, ctx):
        """!adminhelp - DM bot admin command list."""
        admin_cmds = (
            '**!adminhelp** - dm bot admin command list\n'
            '**!load** *<name>* - load extension\n'
            '**!unload** *<name>* - unload extension\n'
            '**!reload** *<name>* - reload extension\n'
            '**!restart** - restart bot'
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
        embed.add_field(name='Pong!', value=f'*Latency:* **{milliseconds}ms**')
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
        embed.add_field(name='📥 Messages Received', value=f'{self.bot.message_count}')
        embed.add_field(name='📤 Messages Sent', value=f'{self.bot.messages_sent}')
        embed.add_field(name='🏷️ Mentions', value=f'{self.bot.mentions_count}')
        embed.add_field(name='💾 Memory Usage', value=f'{mem_usage:.2f} MiB')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
