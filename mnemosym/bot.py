"""
mnemosym.bot
~~~~~~~~~~~~
Discord event handling
"""
import os

from discord.ext import commands
from dotenv import load_dotenv

from mnemosym.chargen import generate_character

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    """print when connecting"""
    print(f"{bot.user.name} has connected to discord!")


@bot.command(name="chargen", help="generates a random character")
async def build_random_character(ctx):
    """builds a random character"""
    await ctx.send(generate_character())


bot.run(TOKEN)
