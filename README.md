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

## Setting up a Discord Application
Before we can invite Mnemosym to our discord channel, we will first need to create a discord application, a bot account, and to note down the OAuth token. These steps can be found in the [documentation for discord.py](https://discordpy.readthedocs.io/en/stable/discord.html).

## Running the back end
```python
# Environment Variables
copy .example_env to .env and modify the file to include the OAuth token from the previous step.  
# Make sure you're using the latest version of the data files.
python scripts/get_tables.py
# Run bot
python -m mnemossym.bot
```

# Docker Container
A Dockerfile has been provided to automate the above build and execution processes.

## Build the docker image
`docker build -t mnemossym .`

## Run the container
`docker run -d mnemossym`

# Aknowledgements

Vaults of Vaarn was created by [Leo Hunt](https://graculusdroog.itch.io/) and licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

Mnemosym's tables are sourced form OmniCzech's [vaarn-generators](https://github.com/omniczech/vaarn-generators).
