from discord import Intents
from discord.ext import commands
import toml


def setup() -> (commands.Bot, dict):
    with open('config.toml') as config_file:
        config = toml.load(config_file)
    intents = Intents.default()
    intents.message_content = True
    return (
        commands.Bot(
            command_prefix=commands.when_mentioned_or("!"),
            intents=intents
        ),
        config
    )
