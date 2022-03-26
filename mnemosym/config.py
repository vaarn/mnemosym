"""
mnemosym.config
~~~~~~~~~~~~~~~
loads .env and stores config variables
"""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
DATA_DIR = Path(os.getenv("DATA_DIR"))
