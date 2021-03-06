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

import math

import discord
from discord.ext import commands

import core.minecraft.hypixel.static.static
import core.minecraft.static
import core.static.static


class Skywars(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="skywars", aliases=["sw"], invoke_without_command=True)
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def skywars(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        player_stats_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Skywars Stats**""",
            color=int((await core.minecraft.hypixel.static.static.get_skywars_prestige_data(
                player_json["skywars"]["level_data"]["level"]))["prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Skywars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Level**__",
            value=f"{player_json['skywars']['level_data']['level']} {core.static.static.star} ({player_json['skywars']['level_data']['percentage']}% to {math.trunc((player_json['skywars']['level_data']['level']) + 1)}) [{(await core.minecraft.hypixel.static.static.get_skywars_prestige_data(player_json['skywars']['level_data']['level']))['prestige']} Prestige]",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Coins**__",
            value=f"{(player_json['skywars']['coins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Tokens**__",
            value=f"{(player_json['skywars']['tokens']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Souls**__",
            value=f"{(player_json['skywars']['souls']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Kills**__",
            value=f"{(player_json['skywars']['kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Deaths**__",
            value=f"{(player_json['skywars']['deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} KDR**__",
            value=f"{(await core.minecraft.hypixel.static.static.get_ratio((player_json['skywars']['kills']), (player_json['skywars']['deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['skywars']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['skywars']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{(await core.minecraft.hypixel.static.static.get_ratio((player_json['skywars']['wins']), (player_json['skywars']['losses'])))}"
        )
        await ctx.send(embed=player_stats_embed)


def setup(bot):
    bot.add_cog(Skywars(bot))
    print("Reloaded cogs.minecraft.hypixel.skywars")
