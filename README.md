# MNEMOSYM
A discord bot for Vaults of Vaarn

# Development
Requirements:
- conda

```python
# Build environment
conda env create -f environment.yml
# activate environment
conda activate mnemosym
# Install git hook scripts
pre-commit install
```

# Running the Bot

```python
# Make sure you're using the latest version of the data files.
python scripts/get_tables.py
# Run bot
python -m mnemossym.bot
```

# Aknowledgements

Vaults of Vaarn was created by [Leo Hunt](https://graculusdroog.itch.io/) and licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

Mnemosym's tables are sourced form OmniCzech's [vaarn-generators](https://github.com/omniczech/vaarn-generators).