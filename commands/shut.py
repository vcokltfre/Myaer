"""
MIT License

Copyright (c) 2020 MyerFire

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import discord
from discord.ext import commands


class Shut(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.shut_url = "https://raw.githubusercontent.com/MyerFire/Myaer/master/core/static/shut.png"

    @commands.command(name="shut")
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def shut(self, ctx):
        await ctx.send(embed=discord.Embed(
            color=ctx.author.color,
            timestamp=ctx.message.created_at
        ).set_image(
            url=self.shut_url
        ))


def setup(bot):
    bot.add_cog(Shut(bot))
    print("Reloaded commands.shut")
