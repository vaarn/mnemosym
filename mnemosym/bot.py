"""
mnemosym.bot
~~~~~~~~~~~~
Discord event handling
"""
from typing import Optional

from discord.ext import commands

import logging

logging.basicConfig(level=logging.INFO)

from mnemosym.config import TOKEN
from mnemosym.generators import (
    generate_ancestry_features,
    generate_armour,
    generate_cybernetic,
    generate_exotica,
    generate_gear,
    generate_gift,
    generate_hp,
    generate_random_character,
    generate_stat_block,
    generate_weapon,
    list_ancestry,
)

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    """print when connecting"""
    print(f"{bot.user.name} has connected to discord!")


@bot.command(name="chargen", help="generates a random character")
async def build_random_character(ctx):
    """builds a random character"""
    await ctx.send(generate_random_character())


@bot.command(
    name="ancestry",
    help=str(
        "Generate a random Ancestry, "
        + "or generate a speciifc one with !ancestry <ancestry> "
        + "(you can find a list of supported ancestries with !ancestry list",
    ),
)
async def build_random_ancestry(ctx, ancestry: Optional[str]):
    """builds a random ancestry"""
    if ancestry == "list":
        await ctx.send(list_ancestry())
    await ctx.send(generate_ancestry_features(ancestry))


@bot.command(name="stats", help="Generate a stat array.")
async def build_stats(ctx):
    """build a statblock"""
    await ctx.send(generate_stat_block())


@bot.command(name="hp", help="Generate hp (1d8), can be fudged with !hp fudge.")
async def build_hp(ctx, fudge: Optional[str]):
    """builds hp, can be fudged"""
    await ctx.send(generate_hp(fudge == "fudge"))


@bot.command(name="weapon", help="Generates a weapon.")
async def build_weapon(ctx):
    """build a weapon string"""
    await ctx.send(generate_weapon())


@bot.command(name="armour", help="Generates armour.")
async def build_armour(ctx):
    """build armour"""
    await ctx.send(generate_armour())


@bot.command(name="gear", help="Generates starting gear (with out !weapon or !armour).")
async def build_gear(ctx):
    """builds starting Gear"""
    await ctx.send(generate_gear())


@bot.command(name="gift", help="Generates gift.")
async def build_gift(ctx):
    """builds gift"""
    await ctx.send(generate_gift())


@bot.command(name="cybernetic", help="Generates cybernetic.")
async def build_cybernetic(ctx):
    """builds gift"""
    await ctx.send(generate_cybernetic())


@bot.command(name="exotica", help="Generates exotica")
async def build_exotica(ctx):
    """builds exotica"""
    await ctx.send(generate_exotica())


bot.run(TOKEN)
