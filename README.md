# MNEMOSYM
A discord bot for Vaults of Vaarn

# Development
Requirements:
- Python >= 3.9
- pip

```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the dependencies
(venv)$ pip install -r requirements-dev.txt
```

# Running the Bot

## Setting up a Discord Application
Before we can invite Mnemosym to our discord channel, we will first need to create a discord application, a bot account, and to note down the OAuth token. These steps can be found in the [documentation for discord.py](https://discordpy.readthedocs.io/en/stable/discord.html).

## Creating the Environment Variables
Copy the `.example_env` file to `.env` and modify it to include the OAuth token from the previous step. This file is used when running the scripts locally, and is passed into the docker container at runtime.

## Running the back end
```bash 
# Make sure you're using the latest version of the data files.
python scripts/get_tables.py
# Run bot
python -m mnemosym.bot
```

# Docker Container
A Dockerfile has been provided to automate the above build and execution processes.

## Build the docker image
`docker build -t mnemosym .`

## Run the container
`docker run --env-file .env -d mnemosym`

# Acknowledgements

Vaults of Vaarn was created by [Leo Hunt](https://graculusdroog.itch.io/) and licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

Mnemosym's tables are sourced form OmniCzech's [vaarn-generators](https://github.com/omniczech/vaarn-generators).
