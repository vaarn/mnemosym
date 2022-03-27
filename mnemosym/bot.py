"""
mnemosym.bot
~~~~~~~~~~~~
Discord event handling
"""
from typing import Optional

from discord.ext import commands

from mnemosym.config import TOKEN
from mnemosym.generators import (
    generate_ancestry_features,
    generate_hp,
    generate_stat_block,
    generate_weapon,
)

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    """print when connecting"""
    print(f"{bot.user.name} has connected to discord!")


@bot.command(name="chargen", help="generates a random character")
async def build_random_character(ctx):
    """builds a random character"""
    # await ctx.send(generate_character())
    raise NotImplementedError


@bot.command(name="ancestry", help="Generate a random Ancestry")
async def build_random_ancestry(ctx):
    """builds a random ancestry"""
    await ctx.send(generate_ancestry_features())


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


bot.run(TOKEN)
