from pathlib import Path

from levibot.config import ConfigLoader

from discord.ext import commands


def main() -> None:
    print("Start")

    bot = commands.Bot(command_prefix="$", self_bot=True)
    bot.owner_ids = [501089151089770517]
    loader = ConfigLoader(Path("work_dir/config.toml"))
    config_data = loader.load()

    bot.load_extension("jishaku")

    bot.run(config_data.token)


if __name__ == "__main__":
    main()
