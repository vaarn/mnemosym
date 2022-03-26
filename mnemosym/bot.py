"""
mnemosym.bot
~~~~~~~~~~~~
Discord event handling
"""
import json
import os
from pathlib import Path
from random import choice

from discord.ext import commands
from dotenv import load_dotenv

from mnemosym.chargen import generate_character
from mnemosym.table_manger import TableManager

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
DATA_DIR = Path(os.getenv("DATA_DIR"))

print("Initalizing Table Manager")
tm = TableManager(DATA_DIR)

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    """print when connecting"""
    print(f"{bot.user.name} has connected to discord!")


@bot.command(name="chargen", help="generates a random character")
async def build_random_character(ctx):
    """builds a random character"""
    await ctx.send(generate_character())


@bot.command(name="ancestry", help="Generate a random Ancestry")
async def build_random_ancestry(ctx):
    """builds a random ancestry"""
    target_ancestry = choice(list(tm.tables["ancestries"].keys()))
    await ctx.send(json.dumps((tm.tables["ancestries"][target_ancestry].roll_table())))


bot.run(TOKEN)
