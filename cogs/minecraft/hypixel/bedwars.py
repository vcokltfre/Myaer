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


class Bedwars(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="bedwars", aliases=["bw"], invoke_without_command=True)
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def bedwars(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_stats_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Bedwars Stats**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Level**__",
            value=f"{player_json['bedwars']['star']} {core.static.static.star} ({(await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json['bedwars']['star']))['prestige']} Prestige)",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Winstreak**__",
            value=f"{(player_json['bedwars']['winstreak']):,d}",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['final_kills']), ((player_json['bedwars']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['beds_broken']), ((player_json['bedwars']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['wins']), ((player_json['bedwars']['losses'])))}"
        )
        await ctx.send(embed=player_stats_embed)

    @bedwars.command(name="stats")  # safety net in case the player"s name is one of the subcommand names
    async def bedwars_stats(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_stats_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Bedwars Stats**""",
            color=int((await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))["prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Level**__",
            value=f"{player_json['bedwars']['star']} {core.static.static.star} ({(await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json['bedwars']['star']))['prestige']} Prestige)",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Winstreak**__",
            value=f"{(player_json['bedwars']['winstreak']):,d}",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['final_kills']), ((player_json['bedwars']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['beds_broken']), ((player_json['bedwars']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['wins']), ((player_json['bedwars']['losses'])))}"
        )
        await ctx.send(embed=player_stats_embed)

    @bedwars.command(name="solo", aliases=["1", "solos"])
    async def solo_bedwars(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_solo_stats_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Solo Bedwars Stats**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Winstreak**__",
            value=f"{(player_json['bedwars']['solo']['winstreak']):,d}",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['solo']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['solo']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['solo']['final_kills']), ((player_json['bedwars']['solo']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['solo']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['solo']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['solo']['beds_broken']), ((player_json['bedwars']['solo']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['solo']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['solo']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['solo']['wins']), ((player_json['bedwars']['solo']['losses'])))}"
        )
        await ctx.send(embed=player_solo_stats_embed)

    @bedwars.command(name="doubles", aliases=["2", "2s", "double", "twos"])
    async def doubles_bedwars(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_doubles_stats_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Doubles Bedwars Stats**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Winstreak**__",
            value=f"{(player_json['bedwars']['doubles']['winstreak']):,d}",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['doubles']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['doubles']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['doubles']['final_kills']), ((player_json['bedwars']['doubles']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['doubles']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['doubles']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['doubles']['beds_broken']), ((player_json['bedwars']['doubles']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['doubles']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['doubles']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['doubles']['wins']), ((player_json['bedwars']['doubles']['losses'])))}"
        )
        await ctx.send(embed=player_doubles_stats_embed)

    @bedwars.command(name="threes", aliases=["3", "3s", "triple", "three"])
    async def threes_bedwars(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_threes_stats_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Threes Bedwars Stats**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Winstreak**__",
            value=f"{(player_json['bedwars']['threes']['winstreak']):,d}",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['threes']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['threes']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['threes']['final_kills']), ((player_json['bedwars']['threes']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['threes']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['threes']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['threes']['beds_broken']), ((player_json['bedwars']['threes']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['threes']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['threes']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['threes']['wins']), ((player_json['bedwars']['threes']['losses'])))}"
        )
        await ctx.send(embed=player_threes_stats_embed)

    @bedwars.command(name="fours", aliases=["4", "4s", "four"])
    async def fours_bedwars(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_fours_stats_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Fours Bedwars Stats**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Winstreak**__",
            value=f"{(player_json['bedwars']['fours']['winstreak']):,d}",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['fours']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['fours']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['fours']['final_kills']), ((player_json['bedwars']['fours']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['fours']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['fours']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['fours']['beds_broken']), ((player_json['bedwars']['fours']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['fours']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['fours']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['fours']['wins']), ((player_json['bedwars']['fours']['losses'])))}"
        )
        await ctx.send(embed=player_fours_stats_embed)

    @bedwars.command(name="4v4")
    async def four_v_four_bedwars(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_four_v_four_stats_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s 4v4 Bedwars Stats**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Winstreak**__",
            value=f"{(player_json['bedwars']['four_v_four']['winstreak']):,d}",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['four_v_four']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['four_v_four']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['four_v_four']['final_kills']), ((player_json['bedwars']['four_v_four']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['four_v_four']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['four_v_four']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['four_v_four']['beds_broken']), ((player_json['bedwars']['four_v_four']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['four_v_four']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['four_v_four']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['four_v_four']['wins']), ((player_json['bedwars']['four_v_four']['losses'])))}"
        )
        await ctx.send(embed=player_four_v_four_stats_embed)

    @bedwars.group(name="armed", invoke_without_command=True)
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def armed(self, ctx):
        return

    @armed.command(name="doubles", aliases=["2", "2s", "double"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def armed_doubles(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_armed_doubles_stats_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Armed Doubles Bedwars Stats**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Winstreak**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['doubles']['winstreak']):,d}",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['doubles']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['doubles']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['armed']['doubles']['final_kills']), ((player_json['bedwars']['dreams']['armed']['doubles']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['doubles']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['doubles']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['armed']['doubles']['beds_broken']), ((player_json['bedwars']['dreams']['armed']['doubles']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['doubles']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['doubles']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['armed']['doubles']['wins']), ((player_json['bedwars']['dreams']['armed']['doubles']['losses'])))}"
        )
        await ctx.send(embed=player_armed_doubles_stats_embed)

    @armed.command(name="fours", aliases=["4", "4s", "four"])
    async def armed_fours(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_armed_fours_stats_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Armed Fours Bedwars Stats**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Winstreak**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['fours']['winstreak']):,d}",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['fours']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['fours']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['armed']['fours']['final_kills']), ((player_json['bedwars']['dreams']['armed']['fours']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['fours']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['fours']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['armed']['fours']['beds_broken']), ((player_json['bedwars']['dreams']['armed']['fours']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['fours']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['fours']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['armed']['fours']['wins']), ((player_json['bedwars']['dreams']['armed']['fours']['losses'])))}"
        )
        await ctx.send(embed=player_armed_fours_stats_embed)

    @bedwars.group(name="castle", aliases=["castles"], invoke_without_command=True)
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def bedwars_castle(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_castle_stats_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Castle Bedwars Stats**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Winstreak**__",
            value=f"{(player_json['bedwars']['dreams']['castle']['winstreak']):,d}",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['castle']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['castle']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['castle']['final_kills']), ((player_json['bedwars']['dreams']['castle']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['castle']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['castle']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['castle']['beds_broken']), ((player_json['bedwars']['dreams']['castle']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['castle']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['castle']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['castle']['wins']), ((player_json['bedwars']['dreams']['castle']['losses'])))}"
        )
        await ctx.send(embed=player_castle_stats_embed)

    @bedwars.group(name="luckyblocks", aliases=["luckyblock", "lucky"], invoke_without_command=True)
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def luckyblocks(self, ctx):
        return

    @luckyblocks.command(name="doubles", aliases=["2s", "2", "double"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def luckyblocks_doubles(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_luckyblocks_doubles_stats_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Luckyblocks Doubles Bedwars Stats**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Winstreak**__",
            value=f"{(player_json['bedwars']['dreams']['lucky_blocks']['doubles']['winstreak']):,d}",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['lucky_blocks']['doubles']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['lucky_blocks']['doubles']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['final_kills']), ((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['lucky_blocks']['doubles']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['lucky_blocks']['doubles']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['beds_broken']), ((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['lucky_blocks']['doubles']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['lucky_blocks']['doubles']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['wins']), ((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['losses'])))}"
        )
        await ctx.send(embed=player_luckyblocks_doubles_stats_embed)

    @luckyblocks.command(name="fours", aliases=["4s", "4"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def luckyblocks_fours(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_luckyblocks_fours_stats_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Luckyblocks Fours Bedwars Stats**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Winstreak**__",
            value=f"{(player_json['bedwars']['dreams']['lucky_blocks']['fours']['winstreak']):,d}",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['lucky_blocks']['fours']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['lucky_blocks']['fours']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['lucky_blocks']['fours']['final_kills']), ((player_json['bedwars']['dreams']['lucky_blocks']['fours']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['lucky_blocks']['fours']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['lucky_blocks']['fours']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['lucky_blocks']['fours']['beds_broken']), ((player_json['bedwars']['dreams']['lucky_blocks']['fours']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['lucky_blocks']['fours']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['lucky_blocks']['fours']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['lucky_blocks']['fours']['wins']), ((player_json['bedwars']['dreams']['lucky_blocks']['fours']['losses'])))}"
        )
        await ctx.send(embed=player_luckyblocks_fours_stats_embed)

    @bedwars.group(name="rush", invoke_without_command=True)
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def rush(self, ctx):
        return

    @rush.command(name="solo", aliases=["1", "solos"])
    async def rush_solo(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_rush_solo_stats_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Rush Solo Bedwars Stats**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Winstreak**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['solo']['winstreak']):,d}",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['solo']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['solo']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['solo']['final_kills']), ((player_json['bedwars']['dreams']['rush']['solo']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['solo']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['solo']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['solo']['beds_broken']), ((player_json['bedwars']['dreams']['rush']['solo']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['solo']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['solo']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['solo']['wins']), ((player_json['bedwars']['dreams']['rush']['solo']['losses'])))}"
        )
        await ctx.send(embed=player_rush_solo_stats_embed)

    @rush.command(name="doubles", aliases=["2", "2s", "double"])
    async def rush_doubles(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_rush_doubles_stats_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Rush Doubles Bedwars Stats**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Winstreak**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['doubles']['winstreak']):,d}",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['doubles']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['doubles']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['doubles']['final_kills']), ((player_json['bedwars']['dreams']['rush']['doubles']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['doubles']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['doubles']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['doubles']['beds_broken']), ((player_json['bedwars']['dreams']['rush']['doubles']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['doubles']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['doubles']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['doubles']['wins']), ((player_json['bedwars']['dreams']['rush']['doubles']['losses'])))}"
        )
        await ctx.send(embed=player_rush_doubles_stats_embed)

    @rush.command(name="fours", aliases=["4", "4s", "four"])
    async def rush_fours(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_rush_fours_stats_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Rush Fours Bedwars Stats**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Winstreak**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['fours']['winstreak']):,d}",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['fours']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['fours']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['fours']['final_kills']), ((player_json['bedwars']['dreams']['rush']['fours']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['fours']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['fours']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['fours']['beds_broken']), ((player_json['bedwars']['dreams']['rush']['fours']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['fours']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['fours']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['fours']['wins']), ((player_json['bedwars']['dreams']['rush']['fours']['losses'])))}"
        )
        await ctx.send(embed=player_rush_fours_stats_embed)

    @bedwars.group(name="ultimate", invoke_without_command=True)
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def ultimate(self, ctx, *args):
        return

    @ultimate.command(name="solo", aliases=["1", "solos"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def ultimate_solo(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_ultimate_solo_stats_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Ultimate Solo Bedwars Stats**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Winstreak**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['solo']['winstreak']):,d}",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['solo']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['solo']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['solo']['final_kills']), ((player_json['bedwars']['dreams']['ultimate']['solo']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['solo']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['solo']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['solo']['beds_broken']), ((player_json['bedwars']['dreams']['ultimate']['solo']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['solo']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['solo']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['solo']['wins']), ((player_json['bedwars']['dreams']['ultimate']['solo']['losses'])))}"
        )
        await ctx.send(embed=player_ultimate_solo_stats_embed)

    @ultimate.command(name="doubles", aliases=["2", "2s", "double"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def ultimate_doubles(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_ultimate_doubles_stats_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Ultimate Doubles Bedwars Stats**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Winstreak**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['doubles']['winstreak']):,d}",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['doubles']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['doubles']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['doubles']['final_kills']), ((player_json['bedwars']['dreams']['ultimate']['doubles']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['doubles']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['doubles']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['doubles']['beds_broken']), ((player_json['bedwars']['dreams']['ultimate']['doubles']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['doubles']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['doubles']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['doubles']['wins']), ((player_json['bedwars']['dreams']['ultimate']['doubles']['losses'])))}"
        )
        await ctx.send(embed=player_ultimate_doubles_stats_embed)

    @ultimate.command(name="fours", aliases=["4", "4s", "four"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def ultimate_fours(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_ultimate_fours_stats_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Ultimate Fours Bedwars Stats**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Winstreak**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['fours']['winstreak']):,d}",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['fours']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['fours']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['fours']['final_kills']), ((player_json['bedwars']['dreams']['ultimate']['fours']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['fours']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['fours']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['fours']['beds_broken']), ((player_json['bedwars']['dreams']['ultimate']['fours']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['fours']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['fours']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['fours']['wins']), ((player_json['bedwars']['dreams']['ultimate']['fours']['losses'])))}"
        )
        await ctx.send(embed=player_ultimate_fours_stats_embed)

    @bedwars.group(name="voidless", invoke_without_command=True)
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def voidless(self, ctx, *args):
        return

    @voidless.command(name="doubles", aliases=["2", "2s", "double"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def voidless_doubles(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_voidless_doubles_stats_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Voidless Doubles Bedwars Stats**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Winstreak**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['doubles']['winstreak']):,d}",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['doubles']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['doubles']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['voidless']['doubles']['final_kills']), ((player_json['bedwars']['dreams']['voidless']['doubles']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['doubles']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['doubles']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['voidless']['doubles']['beds_broken']), ((player_json['bedwars']['dreams']['voidless']['doubles']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['doubles']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['doubles']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['voidless']['doubles']['wins']), ((player_json['bedwars']['dreams']['voidless']['doubles']['losses'])))}"
        )
        await ctx.send(embed=player_voidless_doubles_stats_embed)

    @voidless.command(name="fours", aliases=["4", "4s", "four"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def voidless_fours(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_voidless_fours_stats_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Voidless Fours Bedwars Stats**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Winstreak**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['fours']['winstreak']):,d}",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['fours']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['fours']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['voidless']['fours']['final_kills']), ((player_json['bedwars']['dreams']['voidless']['fours']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['fours']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['fours']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['voidless']['fours']['beds_broken']), ((player_json['bedwars']['dreams']['voidless']['fours']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['fours']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['fours']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['voidless']['fours']['wins']), ((player_json['bedwars']['dreams']['voidless']['fours']['losses'])))}"
        )
        await ctx.send(embed=player_voidless_fours_stats_embed)

    @bedwars.group(name="fkdr", invoke_without_command=True)
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def fkdr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_fkdr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s FKDR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['final_kills']), ((player_json['bedwars']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['final_kills']), (player_json['bedwars']['final_deaths']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['final_kills']), ((player_json['bedwars']['final_deaths'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['final_kills'], player_json['bedwars']['final_deaths']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['final_kills']), (player_json['bedwars']['final_deaths']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['final_kills']), (player_json['bedwars']['final_deaths']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_fkdr_embed)

    @fkdr.command(name="solo", aliases=["1", "solos"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def solo_fkdr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_solo_fkdr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Solo FKDR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['solo']['final_kills']), ((player_json['bedwars']['solo']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['solo']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['solo']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['solo']['final_kills']), (player_json['bedwars']['solo']['final_deaths']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['solo']['final_kills']), ((player_json['bedwars']['solo']['final_deaths'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['solo']['final_kills'], player_json['bedwars']['solo']['final_deaths']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['solo']['final_kills']), (player_json['bedwars']['solo']['final_deaths']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['solo']['final_kills']), (player_json['bedwars']['solo']['final_deaths']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_solo_fkdr_embed)

    @fkdr.command(name="doubles", aliases=["2", "2s", "double"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def doubles_fkdr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_doubles_fkdr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Doubles FKDR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['doubles']['final_kills']), ((player_json['bedwars']['doubles']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['doubles']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['doubles']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['doubles']['final_kills']), (player_json['bedwars']['doubles']['final_deaths']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['doubles']['final_kills']), ((player_json['bedwars']['doubles']['final_deaths'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['doubles']['final_kills'], player_json['bedwars']['doubles']['final_deaths']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['doubles']['final_kills']), (player_json['bedwars']['doubles']['final_deaths']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['doubles']['final_kills']), (player_json['bedwars']['doubles']['final_deaths']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_doubles_fkdr_embed)

    @fkdr.command(name="threes", aliases=["3", "3s", "triple", "three"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def threes_fkdr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_threes_fkdr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Threes FKDR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['threes']['final_kills']), ((player_json['bedwars']['threes']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['threes']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['threes']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['threes']['final_kills']), (player_json['bedwars']['threes']['final_deaths']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['threes']['final_kills']), ((player_json['bedwars']['threes']['final_deaths'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['threes']['final_kills'], player_json['bedwars']['threes']['final_deaths']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['threes']['final_kills']), (player_json['bedwars']['threes']['final_deaths']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['threes']['final_kills']), (player_json['bedwars']['threes']['final_deaths']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_threes_fkdr_embed)

    @fkdr.command(name="fours", aliases=["4", "4s", "four"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def fours_fkdr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_fours_fkdr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Fours FKDR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['fours']['final_kills']), ((player_json['bedwars']['fours']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['fours']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['fours']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['fours']['final_kills']), (player_json['bedwars']['fours']['final_deaths']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['fours']['final_kills']), ((player_json['bedwars']['fours']['final_deaths'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['fours']['final_kills'], player_json['bedwars']['fours']['final_deaths']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['fours']['final_kills']), (player_json['bedwars']['fours']['final_deaths']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['fours']['final_kills']), (player_json['bedwars']['fours']['final_deaths']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_fours_fkdr_embed)

    @fkdr.command(name="4v4")
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def four_v_four_fkdr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_four_v_four_fkdr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s 4v4 FKDR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['four_v_four']['final_kills']), ((player_json['bedwars']['four_v_four']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['four_v_four']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['four_v_four']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['four_v_four']['final_kills']), (player_json['bedwars']['four_v_four']['final_deaths']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['four_v_four']['final_kills']), ((player_json['bedwars']['four_v_four']['final_deaths'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['four_v_four']['final_kills'], player_json['bedwars']['four_v_four']['final_deaths']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['four_v_four']['final_kills']), (player_json['bedwars']['four_v_four']['final_deaths']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['four_v_four']['final_kills']), (player_json['bedwars']['four_v_four']['final_deaths']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_four_v_four_fkdr_embed)

    @fkdr.group(name="armed", invoke_without_command=True)
    async def armed_fkdr(self, ctx):
        return

    @armed_fkdr.command(name="doubles", aliases=["2", "2s", "double"])
    async def armed_doubles_fkdr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_armed_doubles_fkdr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Armed Doubles FKDR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['armed']['doubles']['final_kills']), ((player_json['bedwars']['dreams']['armed']['doubles']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['doubles']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['doubles']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['armed']['doubles']['final_kills']), (player_json['bedwars']['dreams']['armed']['doubles']['final_deaths']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['armed']['doubles']['final_kills']), ((player_json['bedwars']['dreams']['armed']['doubles']['final_deaths'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['armed']['doubles']['final_kills'], player_json['bedwars']['dreams']['armed']['doubles']['final_deaths']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['armed']['doubles']['final_kills']), (player_json['bedwars']['dreams']['armed']['doubles']['final_deaths']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['armed']['doubles']['final_kills']), (player_json['bedwars']['dreams']['armed']['doubles']['final_deaths']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_armed_doubles_fkdr_embed)

    @armed_fkdr.command(name="fours", aliases=["4", "4s", "four"])
    async def armed_fours_fkdr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_armed_fours_fkdr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Armed Fours FKDR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['armed']['fours']['final_kills']), ((player_json['bedwars']['dreams']['armed']['fours']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['fours']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['fours']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['armed']['fours']['final_kills']), (player_json['bedwars']['dreams']['armed']['fours']['final_deaths']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['armed']['fours']['final_kills']), ((player_json['bedwars']['dreams']['armed']['fours']['final_deaths'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['armed']['fours']['final_kills'], player_json['bedwars']['dreams']['armed']['fours']['final_deaths']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['armed']['fours']['final_kills']), (player_json['bedwars']['dreams']['armed']['fours']['final_deaths']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['armed']['fours']['final_kills']), (player_json['bedwars']['dreams']['armed']['fours']['final_deaths']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_armed_fours_fkdr_embed)

    @fkdr.command(name="castle")
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def castle_fkdr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_castle_fkdr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Castle FKDR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['castle']['final_kills']), ((player_json['bedwars']['dreams']['castle']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['castle']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['castle']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['castle']['final_kills']), (player_json['bedwars']['dreams']['castle']['final_deaths']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['castle']['final_kills']), ((player_json['bedwars']['dreams']['castle']['final_deaths'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['castle']['final_kills'], player_json['bedwars']['dreams']['castle']['final_deaths']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['castle']['final_kills']), (player_json['bedwars']['dreams']['castle']['final_deaths']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['castle']['final_kills']), (player_json['bedwars']['dreams']['castle']['final_deaths']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_castle_fkdr_embed)

    @fkdr.group(name="luckyblocks", aliases=["luckyblock", "lucky"], invoke_without_command=True)
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def luckyblocks_fkdr(self, ctx):
        return

    @luckyblocks_fkdr.command(name="doubles", aliases=["2", "2s", "double"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def luckyblocks_doubles_fkdr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_luckyblocks_doubles_fkdr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Luckyblocks Doubles FKDR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['final_kills']), ((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['lucky_blocks']['doubles']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['lucky_blocks']['doubles']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['final_kills']), (player_json['bedwars']['dreams']['lucky_blocks']['doubles']['final_deaths']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['final_kills']), ((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['final_deaths'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['lucky_blocks']['doubles']['final_kills'], player_json['bedwars']['dreams']['lucky_blocks']['doubles']['final_deaths']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['final_kills']), (player_json['bedwars']['dreams']['lucky_blocks']['doubles']['final_deaths']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['final_kills']), (player_json['bedwars']['dreams']['lucky_blocks']['doubles']['final_deaths']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_luckyblocks_doubles_fkdr_embed)

    @luckyblocks_fkdr.command(name="fours", aliases=["4", "4s", "four"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def luckyblocks_fours_fkdr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_luckyblocks_fours_fkdr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Luckyblocks fours FKDR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['lucky_blocks']['fours']['final_kills']), ((player_json['bedwars']['dreams']['lucky_blocks']['fours']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['lucky_blocks']['fours']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['lucky_blocks']['fours']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['lucky_blocks']['fours']['final_kills']), (player_json['bedwars']['dreams']['lucky_blocks']['fours']['final_deaths']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['lucky_blocks']['fours']['final_kills']), ((player_json['bedwars']['dreams']['lucky_blocks']['fours']['final_deaths'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['lucky_blocks']['fours']['final_kills'], player_json['bedwars']['dreams']['lucky_blocks']['fours']['final_deaths']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['lucky_blocks']['fours']['final_kills']), (player_json['bedwars']['dreams']['lucky_blocks']['fours']['final_deaths']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['lucky_blocks']['fours']['final_kills']), (player_json['bedwars']['dreams']['lucky_blocks']['fours']['final_deaths']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_luckyblocks_fours_fkdr_embed)

    @fkdr.group(name="rush", invoke_without_command=True)
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def rush_fkdr(self, ctx):
        return

    @rush_fkdr.command(name="solo", aliases=["1", "solos"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def solo_rush_fkdr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_rush_solo_fkdr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Rush Solo FKDR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['solo']['final_kills']), ((player_json['bedwars']['dreams']['rush']['solo']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['solo']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['solo']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['solo']['final_kills']), (player_json['bedwars']['dreams']['rush']['solo']['final_deaths']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['solo']['final_kills']), ((player_json['bedwars']['dreams']['rush']['solo']['final_deaths'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['rush']['solo']['final_kills'], player_json['bedwars']['dreams']['rush']['solo']['final_deaths']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['solo']['final_kills']), (player_json['bedwars']['dreams']['rush']['solo']['final_deaths']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['solo']['final_kills']), (player_json['bedwars']['dreams']['rush']['solo']['final_deaths']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_rush_solo_fkdr_embed)

    @rush_fkdr.command(name="doubles", aliases=["2", "2s", "double"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def doubles_rush_fkdr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_rush_doubles_fkdr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Rush doubles FKDR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['doubles']['final_kills']), ((player_json['bedwars']['dreams']['rush']['doubles']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['doubles']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['doubles']['final_kills']), (player_json['bedwars']['dreams']['rush']['doubles']['final_deaths']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['doubles']['final_kills']), ((player_json['bedwars']['dreams']['rush']['doubles']['final_deaths'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['rush']['doubles']['final_kills'], player_json['bedwars']['dreams']['rush']['doubles']['final_deaths']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['doubles']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['doubles']['final_kills']), (player_json['bedwars']['dreams']['rush']['doubles']['final_deaths']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['doubles']['final_kills']), (player_json['bedwars']['dreams']['rush']['doubles']['final_deaths']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_rush_doubles_fkdr_embed)

    @rush_fkdr.command(name="fours", aliases=["4", "4s"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def fours_rush_fkdr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_rush_fours_fkdr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Rush Fours FKDR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['fours']['final_kills']), ((player_json['bedwars']['dreams']['rush']['fours']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['fours']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['fours']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['fours']['final_kills']), (player_json['bedwars']['dreams']['rush']['fours']['final_deaths']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['fours']['final_kills']), ((player_json['bedwars']['dreams']['rush']['fours']['final_deaths'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['rush']['fours']['final_kills'], player_json['bedwars']['dreams']['rush']['fours']['final_deaths']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['fours']['final_kills']), (player_json['bedwars']['dreams']['rush']['fours']['final_deaths']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['fours']['final_kills']), (player_json['bedwars']['dreams']['rush']['fours']['final_deaths']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_rush_fours_fkdr_embed)

    @fkdr.group(name="ultimate", aliases=["ultimates"], invoke_without_command=True)
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def ultimate_fkdr(self, ctx):
        return

    @ultimate_fkdr.command(name="solo", aliases=["1", "solos"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def ultimate_solo_fkdr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_ultimate_solo_fkdr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Ultimate Solo FKDR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['solo']['final_kills']), ((player_json['bedwars']['dreams']['ultimate']['solo']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['solo']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['solo']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['solo']['final_kills']), (player_json['bedwars']['dreams']['ultimate']['solo']['final_deaths']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['solo']['final_kills']), ((player_json['bedwars']['dreams']['ultimate']['solo']['final_deaths'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['ultimate']['solo']['final_kills'], player_json['bedwars']['dreams']['ultimate']['solo']['final_deaths']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['solo']['final_kills']), (player_json['bedwars']['dreams']['ultimate']['solo']['final_deaths']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['solo']['final_kills']), (player_json['bedwars']['dreams']['ultimate']['solo']['final_deaths']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_ultimate_solo_fkdr_embed)

    @ultimate_fkdr.command(name="doubles", aliases=["2", "2s", "double"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def ultimate_doubles_fkdr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_ultimate_doubles_fkdr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Ultimate Doubles FKDR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['doubles']['final_kills']), ((player_json['bedwars']['dreams']['ultimate']['doubles']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['doubles']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['doubles']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['doubles']['final_kills']), (player_json['bedwars']['dreams']['ultimate']['doubles']['final_deaths']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['doubles']['final_kills']), ((player_json['bedwars']['dreams']['ultimate']['doubles']['final_deaths'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['ultimate']['doubles']['final_kills'], player_json['bedwars']['dreams']['ultimate']['doubles']['final_deaths']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['doubles']['final_kills']), (player_json['bedwars']['dreams']['ultimate']['doubles']['final_deaths']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['doubles']['final_kills']), (player_json['bedwars']['dreams']['ultimate']['doubles']['final_deaths']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_ultimate_doubles_fkdr_embed)

    @ultimate_fkdr.command(name="fours", aliases=["4", "4s", "four"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def ultimate_fours_fkdr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_ultimate_fours_fkdr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Ultimate Fours FKDR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['fours']['final_kills']), ((player_json['bedwars']['dreams']['ultimate']['fours']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['fours']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['fours']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['fours']['final_kills']), (player_json['bedwars']['dreams']['ultimate']['fours']['final_deaths']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['fours']['final_kills']), ((player_json['bedwars']['dreams']['ultimate']['fours']['final_deaths'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['ultimate']['fours']['final_kills'], player_json['bedwars']['dreams']['ultimate']['fours']['final_deaths']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['fours']['final_kills']), (player_json['bedwars']['dreams']['ultimate']['fours']['final_deaths']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['fours']['final_kills']), (player_json['bedwars']['dreams']['ultimate']['fours']['final_deaths']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_ultimate_fours_fkdr_embed)

    @fkdr.group(name="voidless")
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def voidless_fkdr(self, ctx):
        return

    @voidless_fkdr.command(name="doubles", aliases=["2", "2s", "double"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def voidless_doubles_fkdr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_voidless_doubles_fkdr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Voidless Doubles FKDR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['voidless']['doubles']['final_kills']), ((player_json['bedwars']['dreams']['voidless']['doubles']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['doubles']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['doubles']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['voidless']['doubles']['final_kills']), (player_json['bedwars']['dreams']['voidless']['doubles']['final_deaths']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['voidless']['doubles']['final_kills']), ((player_json['bedwars']['dreams']['voidless']['doubles']['final_deaths'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['voidless']['doubles']['final_kills'], player_json['bedwars']['dreams']['voidless']['doubles']['final_deaths']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['voidless']['doubles']['final_kills']), (player_json['bedwars']['dreams']['voidless']['doubles']['final_deaths']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['voidless']['doubles']['final_kills']), (player_json['bedwars']['dreams']['voidless']['doubles']['final_deaths']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_voidless_doubles_fkdr_embed)

    @voidless_fkdr.command(name="fours", aliases=["4", "4s", "four"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def voidless_fours_fkdr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_voidless_fours_fkdr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Voidless Fours FKDR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['voidless']['fours']['final_kills']), ((player_json['bedwars']['dreams']['voidless']['fours']['final_deaths'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Kills**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['fours']['final_kills']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Final Deaths**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['fours']['final_deaths']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['voidless']['fours']['final_kills']), (player_json['bedwars']['dreams']['voidless']['fours']['final_deaths']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['voidless']['fours']['final_kills']), ((player_json['bedwars']['dreams']['voidless']['fours']['final_deaths'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['voidless']['fours']['final_kills'], player_json['bedwars']['dreams']['voidless']['fours']['final_deaths']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['voidless']['fours']['final_kills']), (player_json['bedwars']['dreams']['voidless']['fours']['final_deaths']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 FKDR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['voidless']['fours']['final_kills']), (player_json['bedwars']['dreams']['voidless']['fours']['final_deaths']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_voidless_fours_fkdr_embed)

    @bedwars.group(name="bblr", invoke_without_command=True)
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def bblr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_bblr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s BBLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['beds_broken']), ((player_json['bedwars']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['beds_broken']), (player_json['bedwars']['beds_lost']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['beds_broken']), ((player_json['bedwars']['beds_lost'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['beds_broken'], player_json['bedwars']['beds_lost']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['beds_broken']), (player_json['bedwars']['beds_lost']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['beds_broken']), (player_json['bedwars']['beds_lost']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_bblr_embed)

    @bblr.command(name="solo", aliases=["1", "solos"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def solo_bblr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_solo_bblr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Solo BBLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['solo']['beds_broken']), ((player_json['bedwars']['solo']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['solo']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['solo']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['solo']['beds_broken']), (player_json['bedwars']['solo']['beds_lost']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['solo']['beds_broken']), ((player_json['bedwars']['solo']['beds_lost'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['solo']['beds_broken'], player_json['bedwars']['solo']['beds_lost']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['solo']['beds_broken']), (player_json['bedwars']['solo']['beds_lost']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['solo']['beds_broken']), (player_json['bedwars']['solo']['beds_lost']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_solo_bblr_embed)

    @bblr.command(name="doubles", aliases=["2", "2s", "double", "twos"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def doubles_bblr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_doubles_bblr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Doubles BBLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['doubles']['beds_broken']), ((player_json['bedwars']['doubles']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['doubles']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['doubles']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['doubles']['beds_broken']), (player_json['bedwars']['doubles']['beds_lost']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['doubles']['beds_broken']), ((player_json['bedwars']['doubles']['beds_lost'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['doubles']['beds_broken'], player_json['bedwars']['doubles']['beds_lost']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['doubles']['beds_broken']), (player_json['bedwars']['doubles']['beds_lost']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['doubles']['beds_broken']), (player_json['bedwars']['doubles']['beds_lost']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_doubles_bblr_embed)

    @bblr.command(name="threes", aliases=["3", "3s", "triple", "three"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def threes_bblr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_threes_bblr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Threes BBLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['threes']['beds_broken']), ((player_json['bedwars']['threes']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['threes']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['threes']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['threes']['beds_broken']), (player_json['bedwars']['threes']['beds_lost']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['threes']['beds_broken']), ((player_json['bedwars']['threes']['beds_lost'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['threes']['beds_broken'], player_json['bedwars']['threes']['beds_lost']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['threes']['beds_broken']), (player_json['bedwars']['threes']['beds_lost']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['threes']['beds_broken']), (player_json['bedwars']['threes']['beds_lost']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_threes_bblr_embed)

    @bblr.command(name="fours", aliases=["4", "4s", "four"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def fours_bblr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_fours_bblr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Fours BBLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['fours']['beds_broken']), ((player_json['bedwars']['fours']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['fours']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['fours']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['fours']['beds_broken']), (player_json['bedwars']['fours']['beds_lost']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['fours']['beds_broken']), ((player_json['bedwars']['fours']['beds_lost'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['fours']['beds_broken'], player_json['bedwars']['fours']['beds_lost']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['fours']['beds_broken']), (player_json['bedwars']['fours']['beds_lost']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['fours']['beds_broken']), (player_json['bedwars']['fours']['beds_lost']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_fours_bblr_embed)

    @bblr.command(name="4v4")
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def four_v_four_bblr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_four_v_four_bblr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s 4v4 BBLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['four_v_four']['beds_broken']), ((player_json['bedwars']['four_v_four']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['four_v_four']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['four_v_four']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['four_v_four']['beds_broken']), (player_json['bedwars']['four_v_four']['beds_lost']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['four_v_four']['beds_broken']), ((player_json['bedwars']['four_v_four']['beds_lost'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['four_v_four']['beds_broken'], player_json['bedwars']['four_v_four']['beds_lost']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['four_v_four']['beds_broken']), (player_json['bedwars']['four_v_four']['beds_lost']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['four_v_four']['beds_broken']), (player_json['bedwars']['four_v_four']['beds_lost']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_four_v_four_bblr_embed)

    @bblr.group(name="armed", invoke_without_command=True)
    async def armed_bblr(self, ctx):
        return

    @armed_bblr.command(name="doubles", aliases=["2", "2s", "double"])
    async def armed_doubles_bblr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_armed_doubles_bblr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Armed Doubles BBLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['armed']['doubles']['beds_broken']), ((player_json['bedwars']['dreams']['armed']['doubles']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['doubles']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['doubles']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['armed']['doubles']['beds_broken']), (player_json['bedwars']['dreams']['armed']['doubles']['beds_lost']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['armed']['doubles']['beds_broken']), ((player_json['bedwars']['dreams']['armed']['doubles']['beds_lost'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['armed']['doubles']['beds_broken'], player_json['bedwars']['dreams']['armed']['doubles']['beds_lost']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['armed']['doubles']['beds_broken']), (player_json['bedwars']['dreams']['armed']['doubles']['beds_lost']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['armed']['doubles']['beds_broken']), (player_json['bedwars']['dreams']['armed']['doubles']['beds_lost']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_armed_doubles_bblr_embed)

    @armed_bblr.command(name="fours", aliases=["4", "4s", "four"])
    async def armed_fours_bblr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_armed_fours_bblr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Armed Fours BBLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['armed']['fours']['beds_broken']), ((player_json['bedwars']['dreams']['armed']['fours']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['fours']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['fours']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['armed']['fours']['beds_broken']), (player_json['bedwars']['dreams']['armed']['fours']['beds_lost']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['armed']['fours']['beds_broken']), ((player_json['bedwars']['dreams']['armed']['fours']['beds_lost'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['armed']['fours']['beds_broken'], player_json['bedwars']['dreams']['armed']['fours']['beds_lost']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['armed']['fours']['beds_broken']), (player_json['bedwars']['dreams']['armed']['fours']['beds_lost']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['armed']['fours']['beds_broken']), (player_json['bedwars']['dreams']['armed']['fours']['beds_lost']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_armed_fours_bblr_embed)

    @bblr.command(name="castle")
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def castle_bblr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_castle_bblr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Castle BBLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['castle']['beds_broken']), ((player_json['bedwars']['dreams']['castle']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['castle']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['castle']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['armed']['doubles']['beds_broken']), (player_json['bedwars']['dreams']['armed']['doubles']['beds_lost']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['armed']['doubles']['beds_broken']), ((player_json['bedwars']['dreams']['armed']['doubles']['beds_lost'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['castle']['beds_broken'], player_json['bedwars']['dreams']['armed']['doubles']['beds_lost']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['castle']['beds_broken']), (player_json['bedwars']['dreams']['castle']['beds_lost']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['castle']['beds_broken']), (player_json['bedwars']['dreams']['castle']['beds_lost']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_castle_bblr_embed)

    @bblr.group(name="luckyblocks", aliases=["luckyblock", "lucky"], invoke_without_command=True)
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def luckyblocks_bblr(self, ctx):
        return

    @luckyblocks_bblr.command(name="doubles", aliases=["2", "2s", "double"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def luckyblocks_doubles_bblr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_luckyblocks_doubles_bblr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Luckyblocks Doubles BBLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['beds_broken']), ((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['lucky_blocks']['doubles']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['lucky_blocks']['doubles']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['beds_broken']), (player_json['bedwars']['dreams']['lucky_blocks']['doubles']['beds_lost']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['beds_broken']), ((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['beds_lost'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['lucky_blocks']['doubles']['beds_broken'], player_json['bedwars']['dreams']['lucky_blocks']['doubles']['beds_lost']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['beds_broken']), (player_json['bedwars']['dreams']['lucky_blocks']['doubles']['beds_lost']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['beds_broken']), (player_json['bedwars']['dreams']['lucky_blocks']['doubles']['beds_lost']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_luckyblocks_doubles_bblr_embed)

    @luckyblocks_bblr.command(name="fours", aliases=["4", "4s", "four"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def luckyblocks_fours_bblr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_luckyblocks_fours_bblr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Luckyblocks fours BBLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['lucky_blocks']['fours']['beds_broken']), ((player_json['bedwars']['dreams']['lucky_blocks']['fours']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['lucky_blocks']['fours']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['lucky_blocks']['fours']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['lucky_blocks']['fours']['beds_broken']), (player_json['bedwars']['dreams']['lucky_blocks']['fours']['beds_lost']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['lucky_blocks']['fours']['beds_broken']), ((player_json['bedwars']['dreams']['lucky_blocks']['fours']['beds_lost'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['lucky_blocks']['fours']['beds_broken'], player_json['bedwars']['dreams']['lucky_blocks']['fours']['beds_lost']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['lucky_blocks']['fours']['beds_broken']), (player_json['bedwars']['dreams']['lucky_blocks']['fours']['beds_lost']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['lucky_blocks']['fours']['beds_broken']), (player_json['bedwars']['dreams']['lucky_blocks']['fours']['beds_lost']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_luckyblocks_fours_bblr_embed)

    @bblr.group(name="rush", invoke_without_command=True)
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def rush_bblr(self, ctx):
        return

    @rush_bblr.command(name="solo", aliases=["1", "solos"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def solo_rush_bblr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_rush_solo_bblr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Rush Solo BBLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['solo']['beds_broken']), ((player_json['bedwars']['dreams']['rush']['solo']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['solo']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['solo']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['solo']['beds_broken']), (player_json['bedwars']['dreams']['rush']['solo']['beds_lost']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['solo']['beds_broken']), ((player_json['bedwars']['dreams']['rush']['solo']['beds_lost'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['rush']['solo']['beds_broken'], player_json['bedwars']['dreams']['rush']['solo']['beds_lost']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['solo']['beds_broken']), (player_json['bedwars']['dreams']['rush']['solo']['beds_lost']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['solo']['beds_broken']), (player_json['bedwars']['dreams']['rush']['solo']['beds_lost']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_rush_solo_bblr_embed)

    @rush_bblr.command(name="doubles", aliases=["2", "2s", "double"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def doubles_rush_bblr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_rush_doubles_bblr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Rush doubles BBLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['doubles']['beds_broken']), ((player_json['bedwars']['dreams']['rush']['doubles']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['doubles']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['doubles']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['doubles']['beds_broken']), (player_json['bedwars']['dreams']['rush']['doubles']['beds_lost']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['doubles']['beds_broken']), ((player_json['bedwars']['dreams']['rush']['doubles']['beds_lost'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['rush']['doubles']['beds_broken'], player_json['bedwars']['dreams']['rush']['doubles']['beds_lost']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['doubles']['beds_broken']), (player_json['bedwars']['dreams']['rush']['doubles']['beds_lost']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['doubles']['beds_broken']), (player_json['bedwars']['dreams']['rush']['doubles']['beds_lost']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_rush_doubles_bblr_embed)

    @rush_bblr.command(name="fours", aliases=["4", "4s"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def fours_rush_bblr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_rush_fours_bblr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Rush Fours BBLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['fours']['beds_broken']), ((player_json['bedwars']['dreams']['rush']['fours']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['fours']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['fours']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['fours']['beds_broken']), (player_json['bedwars']['dreams']['rush']['fours']['beds_lost']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['fours']['beds_broken']), ((player_json['bedwars']['dreams']['rush']['fours']['beds_lost'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['rush']['fours']['beds_broken'], player_json['bedwars']['dreams']['rush']['fours']['beds_lost']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['fours']['beds_broken']), (player_json['bedwars']['dreams']['rush']['fours']['beds_lost']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['fours']['beds_broken']), (player_json['bedwars']['dreams']['rush']['fours']['beds_lost']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_rush_fours_bblr_embed)

    @bblr.group(name="ultimate", aliases=["ultimates"], invoke_without_command=True)
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def ultimate_bblr(self, ctx):
        return

    @ultimate_bblr.command(name="solo", aliases=["1", "solos"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def ultimate_solo_bblr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_ultimate_solo_bblr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Ultimate Solo BBLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['solo']['beds_broken']), ((player_json['bedwars']['dreams']['ultimate']['solo']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['solo']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['solo']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['solo']['beds_broken']), (player_json['bedwars']['dreams']['ultimate']['solo']['beds_lost']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['solo']['beds_broken']), ((player_json['bedwars']['dreams']['ultimate']['solo']['beds_lost'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['ultimate']['solo']['beds_broken'], player_json['bedwars']['dreams']['ultimate']['solo']['beds_lost']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['solo']['beds_broken']), (player_json['bedwars']['dreams']['ultimate']['solo']['beds_lost']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['solo']['beds_broken']), (player_json['bedwars']['dreams']['ultimate']['solo']['beds_lost']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_ultimate_solo_bblr_embed)

    @ultimate_bblr.command(name="doubles", aliases=["2", "2s", "double"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def ultimate_doubles_bblr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_ultimate_doubles_bblr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Ultimate Doubles BBLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['doubles']['beds_broken']), ((player_json['bedwars']['dreams']['ultimate']['doubles']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['doubles']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['doubles']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['doubles']['beds_broken']), (player_json['bedwars']['dreams']['ultimate']['doubles']['beds_lost']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['doubles']['beds_broken']), ((player_json['bedwars']['dreams']['ultimate']['doubles']['beds_lost'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['ultimate']['doubles']['beds_broken'], player_json['bedwars']['dreams']['ultimate']['doubles']['beds_lost']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['doubles']['beds_broken']), (player_json['bedwars']['dreams']['ultimate']['doubles']['beds_lost']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['doubles']['beds_broken']), (player_json['bedwars']['dreams']['ultimate']['doubles']['beds_lost']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_ultimate_doubles_bblr_embed)

    @ultimate_bblr.command(name="fours", aliases=["4", "4s", "four"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def ultimate_fours_bblr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_ultimate_fours_bblr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Ultimate Fours BBLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['fours']['beds_broken']), ((player_json['bedwars']['dreams']['ultimate']['fours']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['fours']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['fours']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['fours']['beds_broken']), (player_json['bedwars']['dreams']['ultimate']['fours']['beds_lost']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['fours']['beds_broken']), ((player_json['bedwars']['dreams']['ultimate']['fours']['beds_lost'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['ultimate']['fours']['beds_broken'], player_json['bedwars']['dreams']['ultimate']['fours']['beds_lost']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['fours']['beds_broken']), (player_json['bedwars']['dreams']['ultimate']['fours']['beds_lost']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['fours']['beds_broken']), (player_json['bedwars']['dreams']['ultimate']['fours']['beds_lost']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_ultimate_fours_bblr_embed)

    @bblr.group(name="voidless")
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def voidless_bblr(self, ctx):
        return

    @voidless_bblr.command(name="doubles", aliases=["2", "2s", "double"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def voidless_doubles_bblr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_voidless_doubles_bblr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Voidless Doubles BBLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['voidless']['doubles']['beds_broken']), ((player_json['bedwars']['dreams']['voidless']['doubles']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['doubles']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['doubles']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['voidless']['doubles']['beds_broken']), (player_json['bedwars']['dreams']['voidless']['doubles']['beds_lost']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['voidless']['doubles']['beds_broken']), ((player_json['bedwars']['dreams']['voidless']['doubles']['beds_lost'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['voidless']['doubles']['beds_broken'], player_json['bedwars']['dreams']['voidless']['doubles']['beds_lost']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['voidless']['doubles']['beds_broken']), (player_json['bedwars']['dreams']['voidless']['doubles']['beds_lost']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['voidless']['doubles']['beds_broken']), (player_json['bedwars']['dreams']['voidless']['doubles']['beds_lost']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_voidless_doubles_bblr_embed)

    @voidless_bblr.command(name="fours", aliases=["4", "4s", "four"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def voidless_fours_bblr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_voidless_fours_bblr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Voidless Fours BBLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['voidless']['fours']['beds_broken']), ((player_json['bedwars']['dreams']['voidless']['fours']['beds_lost'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Broken**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['fours']['beds_broken']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Beds Lost**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['fours']['beds_lost']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['voidless']['fours']['beds_broken']), (player_json['bedwars']['dreams']['voidless']['fours']['beds_lost']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['voidless']['fours']['beds_broken']), ((player_json['bedwars']['dreams']['voidless']['fours']['beds_lost'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['voidless']['fours']['beds_broken'], player_json['bedwars']['dreams']['voidless']['fours']['beds_lost']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['voidless']['fours']['beds_broken']), (player_json['bedwars']['dreams']['voidless']['fours']['beds_lost']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 BBLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['voidless']['fours']['beds_broken']), (player_json['bedwars']['dreams']['voidless']['fours']['beds_lost']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_voidless_fours_bblr_embed)

    @bedwars.group(name="wlr", invoke_without_command=True)
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def wlr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_wlr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s WLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['wins']), ((player_json['bedwars']['losses'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['wins']), (player_json['bedwars']['losses']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['wins']), ((player_json['bedwars']['losses'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['wins'], player_json['bedwars']['losses']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['wins']), (player_json['bedwars']['losses']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['wins']), (player_json['bedwars']['losses']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_wlr_embed)

    @wlr.command(name="solo", aliases=["1", "solos"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def solo_wlr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_solo_wlr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Solo WLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['solo']['wins']), ((player_json['bedwars']['solo']['losses'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['solo']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['solo']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['solo']['wins']), (player_json['bedwars']['solo']['losses']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['solo']['wins']), ((player_json['bedwars']['solo']['losses'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['solo']['wins'], player_json['bedwars']['solo']['losses']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['solo']['wins']), (player_json['bedwars']['solo']['losses']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['solo']['wins']), (player_json['bedwars']['solo']['losses']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_solo_wlr_embed)

    @wlr.command(name="doubles", aliases=["2", "2s", "double", "twos"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def doubles_wlr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_doubles_wlr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Doubles WLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['doubles']['wins']), ((player_json['bedwars']['doubles']['losses'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['doubles']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['doubles']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['doubles']['wins']), (player_json['bedwars']['doubles']['losses']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['doubles']['wins']), ((player_json['bedwars']['doubles']['losses'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['doubles']['wins'], player_json['bedwars']['doubles']['losses']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['doubles']['wins']), (player_json['bedwars']['doubles']['losses']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['doubles']['wins']), (player_json['bedwars']['doubles']['losses']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_doubles_wlr_embed)

    @wlr.command(name="threes", aliases=["3", "3s", "triple", "three"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def threes_wlr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_threes_wlr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Threes WLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['trees']['wins']), ((player_json['bedwars']['threes']['losses'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{player_json['trees']['wins']}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['threes']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['threes']['wins']), (player_json['bedwars']['threes']['losses']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['threes']['wins']), ((player_json['bedwars']['threes']['losses'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['threes']['wins'], player_json['bedwars']['threes']['losses']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['trees']['wins']), (player_json['bedwars']['threes']['losses']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['trees']['wins']), (player_json['bedwars']['threes']['losses']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_threes_wlr_embed)

    @wlr.command(name="fours", aliases=["4", "4s", "four"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def fours_wlr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_fours_wlr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Fours WLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['fours']['wins']), ((player_json['bedwars']['fours']['losses'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['fours']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['fours']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['fours']['wins']), (player_json['bedwars']['fours']['losses']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['fours']['wins']), ((player_json['bedwars']['fours']['losses'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['fours']['wins'], player_json['bedwars']['fours']['losses']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['fours']['wins']), (player_json['bedwars']['fours']['losses']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['fours']['wins']), (player_json['bedwars']['fours']['losses']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_fours_wlr_embed)

    @wlr.command(name="4v4")
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def four_v_four_wlr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_four_v_four_wlr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s 4v4 WLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['four_v_four']['wins']), ((player_json['bedwars']['four_v_four']['losses'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['four_v_four']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['four_v_four']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['four_v_four']['wins']), (player_json['bedwars']['four_v_four']['losses']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['four_v_four']['wins']), ((player_json['bedwars']['four_v_four']['losses'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['four_v_four']['wins'], player_json['bedwars']['four_v_four']['losses']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['four_v_four']['wins']), (player_json['bedwars']['four_v_four']['losses']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['four_v_four']['wins']), (player_json['bedwars']['four_v_four']['losses']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_four_v_four_wlr_embed)

    @wlr.group(name="armed", invoke_without_command=True)
    async def armed_wlr(self, ctx):
        return

    @armed_wlr.command(name="doubles", aliases=["2", "2s", "double"])
    async def armed_doubles_wlr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_armed_doubles_wlr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Armed Doubles WLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['armed']['doubles']['wins']), ((player_json['bedwars']['dreams']['armed']['doubles']['losses'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['doubles']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['doubles']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['armed']['doubles']['wins']), (player_json['bedwars']['dreams']['armed']['doubles']['losses']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['armed']['doubles']['wins']), ((player_json['bedwars']['dreams']['armed']['doubles']['losses'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['armed']['doubles']['wins'], player_json['bedwars']['dreams']['armed']['doubles']['losses']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['armed']['doubles']['wins']), (player_json['bedwars']['dreams']['armed']['doubles']['losses']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['armed']['doubles']['wins']), (player_json['bedwars']['dreams']['armed']['doubles']['losses']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_armed_doubles_wlr_embed)

    @armed_wlr.command(name="fours", aliases=["4", "4s", "four"])
    async def armed_fours_wlr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_armed_fours_wlr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Armed Fours WLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['armed']['fours']['wins']), ((player_json['bedwars']['dreams']['armed']['fours']['losses'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['fours']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['armed']['fours']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['armed']['fours']['wins']), (player_json['bedwars']['dreams']['armed']['fours']['losses']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['armed']['fours']['wins']), ((player_json['bedwars']['dreams']['armed']['fours']['losses'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['armed']['fours']['wins'], player_json['bedwars']['dreams']['armed']['fours']['losses']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['armed']['fours']['wins']), (player_json['bedwars']['dreams']['armed']['fours']['losses']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['armed']['fours']['wins']), (player_json['bedwars']['dreams']['armed']['fours']['losses']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_armed_fours_wlr_embed)

    @wlr.command(name="castle")
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def castle_wlr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_castle_wlr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Castle WLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['castle']['wins']), ((player_json['bedwars']['dreams']['castle']['losses'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['castle']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['castle']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['castle']['wins']), (player_json['bedwars']['dreams']['castle']['losses']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['castle']['wins']), ((player_json['bedwars']['dreams']['castle']['losses'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['castle']['wins'], player_json['bedwars']['dreams']['castle']['losses']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['castle']['wins']), (player_json['bedwars']['dreams']['castle']['losses']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['castle']['wins']), (player_json['bedwars']['dreams']['castle']['losses']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_castle_wlr_embed)

    @wlr.group(name="luckyblocks", aliases=["luckyblock", "lucky"], invoke_without_command=True)
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def luckyblocks_wlr(self, ctx):
        return

    @luckyblocks_wlr.command(name="doubles", aliases=["2", "2s", "double"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def luckyblocks_doubles_wlr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_luckyblocks_doubles_wlr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Luckyblocks Doubles WLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['wins']), ((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['losses'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['lucky_blocks']['doubles']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['lucky_blocks']['doubles']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['wins']), (player_json['bedwars']['dreams']['lucky_blocks']['doubles']['losses']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['wins']), ((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['losses'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['lucky_blocks']['doubles']['wins'], player_json['bedwars']['dreams']['lucky_blocks']['doubles']['losses']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['wins']), (player_json['bedwars']['dreams']['lucky_blocks']['doubles']['losses']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['lucky_blocks']['doubles']['wins']), (player_json['bedwars']['dreams']['lucky_blocks']['doubles']['losses']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_luckyblocks_doubles_wlr_embed)

    @wlr.group(name="rush", invoke_without_command=True)
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def rush_wlr(self, ctx):
        return

    @rush_wlr.command(name="solo", aliases=["1", "solos"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def solo_rush_wlr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_rush_solo_wlr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Rush Solo WLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['solo']['wins']), ((player_json['bedwars']['dreams']['rush']['solo']['losses'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['solo']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['solo']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['solo']['wins']), (player_json['bedwars']['dreams']['rush']['solo']['losses']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['solo']['wins']), ((player_json['bedwars']['dreams']['rush']['solo']['losses'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['rush']['solo']['wins'], player_json['bedwars']['dreams']['rush']['solo']['losses']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['solo']['wins']), (player_json['bedwars']['dreams']['rush']['solo']['losses']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['solo']['wins']), (player_json['bedwars']['dreams']['rush']['solo']['losses']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_rush_solo_wlr_embed)

    @rush_wlr.command(name="doubles", aliases=["2", "2s", "double"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def doubles_rush_wlr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_rush_doubles_wlr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Rush Doubles WLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['doubles']['wins']), ((player_json['bedwars']['dreams']['rush']['doubles']['losses'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['doubles']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['doubles']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['doubles']['wins']), (player_json['bedwars']['dreams']['rush']['doubles']['losses']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['doubles']['wins']), ((player_json['bedwars']['dreams']['rush']['doubles']['losses'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['rush']['doubles']['wins'], player_json['bedwars']['dreams']['rush']['doubles']['losses']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['doubles']['wins']), (player_json['bedwars']['dreams']['rush']['doubles']['losses']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['doubles']['wins']), (player_json['bedwars']['dreams']['rush']['doubles']['losses']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_rush_doubles_wlr_embed)

    @rush_wlr.command(name="fours", aliases=["4", "4s"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def fours_rush_wlr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_rush_fours_wlr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Rush Fours WLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['fours']['wins']), ((player_json['bedwars']['dreams']['rush']['fours']['losses'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['fours']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['rush']['fours']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['fours']['wins']), (player_json['bedwars']['dreams']['rush']['fours']['losses']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['rush']['fours']['wins']), ((player_json['bedwars']['dreams']['rush']['fours']['losses'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['rush']['fours']['wins'], player_json['bedwars']['dreams']['rush']['fours']['losses']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['fours']['wins']), (player_json['bedwars']['dreams']['rush']['fours']['losses']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['rush']['fours']['wins']), (player_json['bedwars']['dreams']['rush']['fours']['losses']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_rush_fours_wlr_embed)

    @wlr.group(name="ultimate", aliases=["ultimates"], invoke_without_command=True)
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def ultimate_wlr(self, ctx):
        return

    @ultimate_wlr.command(name="solo", aliases=["1", "solos"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def ultimate_solo_wlr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_ultimate_solo_wlr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Ultimate Solo WLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['solo']['wins']), ((player_json['bedwars']['dreams']['ultimate']['solo']['losses'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['solo']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['solo']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['solo']['wins']), (player_json['bedwars']['dreams']['ultimate']['solo']['losses']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['solo']['wins']), ((player_json['bedwars']['dreams']['ultimate']['solo']['losses'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['ultimate']['solo']['wins'], player_json['bedwars']['dreams']['ultimate']['solo']['losses']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['solo']['wins']), (player_json['bedwars']['dreams']['ultimate']['solo']['losses']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['solo']['wins']), (player_json['bedwars']['dreams']['ultimate']['solo']['losses']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_ultimate_solo_wlr_embed)

    @ultimate_wlr.command(name="doubles", aliases=["2", "2s", "double"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def ultimate_doubles_wlr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_ultimate_doubles_wlr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Ultimate Doubles WLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['doubles']['wins']), ((player_json['bedwars']['dreams']['ultimate']['doubles']['losses'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['doubles']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['doubles']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['doubles']['wins']), (player_json['bedwars']['dreams']['ultimate']['doubles']['losses']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['doubles']['wins']), ((player_json['bedwars']['dreams']['ultimate']['doubles']['losses'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['ultimate']['doubles']['wins'], player_json['bedwars']['dreams']['ultimate']['doubles']['losses']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['doubles']['wins']), (player_json['bedwars']['dreams']['ultimate']['doubles']['losses']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['doubles']['wins']), (player_json['bedwars']['dreams']['ultimate']['doubles']['losses']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_ultimate_doubles_wlr_embed)

    @ultimate_wlr.command(name="fours", aliases=["4", "4s", "four"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def ultimate_fours_wlr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_ultimate_fours_wlr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Ultimate Fours WLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['fours']['wins']), ((player_json['bedwars']['dreams']['ultimate']['fours']['losses'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['fours']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['ultimate']['fours']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['fours']['wins']), (player_json['bedwars']['dreams']['ultimate']['fours']['losses']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['ultimate']['fours']['wins']), ((player_json['bedwars']['dreams']['ultimate']['fours']['losses'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['ultimate']['fours']['wins'], player_json['bedwars']['dreams']['ultimate']['fours']['losses']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['fours']['wins']), (player_json['bedwars']['dreams']['ultimate']['fours']['losses']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['ultimate']['fours']['wins']), (player_json['bedwars']['dreams']['ultimate']['fours']['losses']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_ultimate_fours_wlr_embed)

    @wlr.group(name="voidless")
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def voidless_wlr(self, ctx):
        return

    @voidless_wlr.command(name="doubles", aliases=["2", "2s", "double"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def voidless_doubles_wlr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_voidless_doubles_wlr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Voidless Doubles WLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['voidless']['doubles']['wins']), ((player_json['bedwars']['dreams']['voidless']['doubles']['losses'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['doubles']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['doubles']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['voidless']['doubles']['wins']), (player_json['bedwars']['dreams']['voidless']['doubles']['losses']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['voidless']['doubles']['wins']), ((player_json['bedwars']['dreams']['voidless']['doubles']['losses'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['voidless']['doubles']['wins'], player_json['bedwars']['dreams']['voidless']['doubles']['losses']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['voidless']['doubles']['wins']), (player_json['bedwars']['dreams']['voidless']['doubles']['losses']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['voidless']['doubles']['wins']), (player_json['bedwars']['dreams']['voidless']['doubles']['losses']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_voidless_doubles_wlr_embed)

    @voidless_wlr.command(name="fours", aliases=["4", "4s", "four"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def voidless_fours_wlr(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        player_voidless_fours_wlr_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}" if player_json["rank_data"]["rank"] else player_data["player_formatted_name"])}'s Voidless Fours WLR**""",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16)  # 16 - Hex value.
        ).set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['voidless']['fours']['wins']), ((player_json['bedwars']['dreams']['voidless']['fours']['losses'])))}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Wins**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['fours']['wins']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Losses**__",
            value=f"{(player_json['bedwars']['dreams']['voidless']['fours']['losses']):,d}"
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} Next 1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['voidless']['fours']['wins']), (player_json['bedwars']['dreams']['voidless']['fours']['losses']), ((math.trunc(await core.minecraft.hypixel.static.static.get_ratio((player_json['bedwars']['dreams']['voidless']['fours']['wins']), ((player_json['bedwars']['dreams']['voidless']['fours']['losses'])))) + 1) - (await core.minecraft.hypixel.static.static.get_ratio(player_json['bedwars']['dreams']['voidless']['fours']['wins'], player_json['bedwars']['dreams']['voidless']['fours']['losses']))))} needed"
            # don't ask, cause i don't know either; this is for the next integer value
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +1 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['voidless']['fours']['wins']), (player_json['bedwars']['dreams']['voidless']['fours']['losses']), 1)} needed",
            inline=False
        ).add_field(
            name=f"__**{core.static.static.arrow_bullet_point} +2 WLR**__",
            value=f"{await core.minecraft.hypixel.static.static.get_increase_stat((player_json['bedwars']['dreams']['voidless']['fours']['wins']), (player_json['bedwars']['dreams']['voidless']['fours']['losses']), 2)} needed"
        ).set_footer(
            text=core.static.static.stats_needed_disclaimer
        )
        await ctx.send(embed=player_voidless_fours_wlr_embed)

    @bedwars.command(name="winstreaks", aliases=["winstreak", "ws"])
    @commands.max_concurrency(1, per=commands.BucketType.user)
    async def winstreaks(self, ctx, *args):
        player_info = await core.minecraft.static.hypixel_name_handler(ctx, args)
        if player_info:
            player_data = player_info["player_data"]
            player_json = player_info["player_json"]
        else:
            return
        await ctx.channel.trigger_typing()
        winstreak_embed = discord.Embed(
            title=f"""**{discord.utils.escape_markdown(f"[{player_json['rank_data']['rank']}] {player_data['player_formatted_name']}")}'s Winstreaks**""" if (
                player_json["rank_data"][
                    "rank"]) else f"**{discord.utils.escape_markdown(player_data['player_formatted_name'])}'s Winstreaks**",
            color=int(
                (await core.minecraft.hypixel.static.static.get_bedwars_prestige_data(player_json["bedwars"]["star"]))[
                    "prestige_color"], 16),  # 16 - Hex value.
            description=
            f"""__**{core.static.static.arrow_bullet_point} Overall**__: {player_json['bedwars']['winstreak']}
__**{core.static.static.arrow_bullet_point} Solo**__: {player_json['bedwars']['solo']['winstreak']}
__**{core.static.static.arrow_bullet_point} Doubles**__: {player_json['bedwars']['doubles']['winstreak']}
__**{core.static.static.arrow_bullet_point} Threes**__: {player_json['bedwars']['threes']['winstreak']}
__**{core.static.static.arrow_bullet_point} Fours**__: {player_json['bedwars']['fours']['winstreak']}
__**{core.static.static.arrow_bullet_point} 4v4**__: {player_json['bedwars']['four_v_four']['winstreak']}
__**{core.static.static.arrow_bullet_point} Armed Doubles**__: {player_json['bedwars']['dreams']['armed']['doubles']['winstreak']}
__**{core.static.static.arrow_bullet_point} Armed Fours**__: {player_json['bedwars']['dreams']['armed']['fours']['winstreak']}
__**{core.static.static.arrow_bullet_point} Castle**__: {player_json['bedwars']['dreams']['castle']['winstreak']}
__**{core.static.static.arrow_bullet_point} Lucky Blocks Doubles**__: {player_json['bedwars']['dreams']['lucky_blocks']['doubles']['winstreak']}
__**{core.static.static.arrow_bullet_point} Lucky Blocks Fours**__: {player_json['bedwars']['dreams']['lucky_blocks']['fours']['winstreak']}
__**{core.static.static.arrow_bullet_point} Rush Solo**__: {player_json['bedwars']['dreams']['rush']['solo']['winstreak']}
__**{core.static.static.arrow_bullet_point} Rush Doubles**__: {player_json['bedwars']['dreams']['rush']['doubles']['winstreak']}
__**{core.static.static.arrow_bullet_point} Rush Fours**__: {player_json['bedwars']['dreams']['rush']['fours']['winstreak']}
__**{core.static.static.arrow_bullet_point} Ultimate Solo**__: {player_json['bedwars']['dreams']['ultimate']['solo']['winstreak']}
__**{core.static.static.arrow_bullet_point} Ultimate Doubles**__: {player_json['bedwars']['dreams']['ultimate']['doubles']['winstreak']}
__**{core.static.static.arrow_bullet_point} Ultimate Fours**__: {player_json['bedwars']['dreams']['ultimate']['fours']['winstreak']}
__**{core.static.static.arrow_bullet_point} Voidless Doubles**__: {player_json['bedwars']['dreams']['voidless']['doubles']['winstreak']}
__**{core.static.static.arrow_bullet_point} Voidless Fours**__: {player_json['bedwars']['dreams']['voidless']['fours']['winstreak']}"""
        )
        winstreak_embed.set_thumbnail(
            url=core.minecraft.hypixel.static.static.hypixel_icons["Bedwars"]
        )
        await ctx.send(embed=winstreak_embed)


def setup(bot):
    bot.add_cog(Bedwars(bot))
    print("Reloaded cogs.minecraft.hypixel.bedwars")
