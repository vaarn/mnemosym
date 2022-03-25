"""
mnemosym.bot
~~~~~~~~~~~~
Discord event handling
"""
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    """print when connecting"""
    print(f"{bot.user.name} has connected to discord!")


bot.run(TOKEN)
