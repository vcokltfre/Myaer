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

from discord.ext import commands, menus
import discord
from core.paginators import ListPageSource
import core.minecraft.static
import core.minecraft.hypixel.static

class Friends(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command("friends")
	@commands.max_concurrency(1, per = commands.BucketType.user)
	async def friends(self, ctx, *args):
		await ctx.trigger_typing()
		player_info = await core.minecraft.static.hypixel_name_handler(ctx, args, get_friends = True)
		if player_info:
			player_data = player_info["player_data"]
			player_json = player_info["player_json"]
		else: return
		friends_string = []
		for friend in player_json["friends"]:
			friends_string.append(f"""{discord.utils.escape_markdown(f"[{friend['rank_data']['rank']}] {friend['name']}" if friend["rank_data"]["rank"] else friend["name"])}""")
		friends_paginator = menus.MenuPages(source = ListPageSource(friends_string), clear_reactions_after = True)
		await friends_paginator.start(ctx)

def setup(bot):
	bot.add_cog(Friends(bot))
	print("Reloaded cogs.minecraft.hypixel.friends")
