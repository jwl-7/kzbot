"""Info

This module contains information commands.
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
        """!kzbotstatus - KZBOT stats."""
        uptime = time.time() - self.bot.uptime
        minutes, seconds = divmod(uptime, 60)
        hours, minutes = divmod(minutes, 60)

        process = psutil.Process(os.getpid())
        mem_usage = process.memory_info().rss
        mem_usage /= 1024 ** 2

        embed = discord.Embed(
            colour=discord.Colour.green(),
            title='KZBOT - Stats'
        )
        embed.set_thumbnail(url=self.bot.user.avatar_url)
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
