from pathlib import Path

from levibot.config import ConfigLoader

from discord.ext import commands


def main() -> None:
    print("Start")

    loader = ConfigLoader(Path("config.toml"))
    config_data = loader.load()

    bot = commands.Bot(command_prefix=config_data.prefix, self_bot=True)
    bot.owner_ids = config_data.owner_ids


    bot.load_extension("jishaku")


    bot.run(config_data.token)


if __name__ == "__main__":
    main()
