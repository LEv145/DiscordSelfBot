from __future__ import annotations

import os
from pathlib import Path

from levibot.config import ConfigLoader, JishakuConfig

from discord.ext import commands
from jishaku.help_command import DefaultPaginatorHelp


def set_jishaku_environ(config: JishakuConfig) -> None:
    if config.retain:
        os.environ["JISHAKU_RETAIN"] = "true"
    if config.no_underscore_prefix:
        os.environ["JISHAKU_NO_UNDERSCORE"] = "true"
    if config.force_paginator:
        os.environ["JISHAKU_FORCE_PAGINATOR"] = "true"
    if config.always_dm_traceback:
        os.environ["JISHAKU_ALWAYS_DM_TRACEBACK"] = "true"
    if config.no_dm_traceback:
        os.environ["JISHAKU_NO_DM_TRACEBACK"] = "true"
    if config.use_ansi_always:
        os.environ["JISHAKU_USE_ANSI_ALWAYS"] = "true"
    if config.use_ansi_never:
        os.environ["JISHAKU_USE_ANSI_NEVER"] = "false"


def main() -> None:
    print("Start")

    loader = ConfigLoader(Path("config.toml"))
    config_data = loader.load()

    if config_data.jishaku_config:
        set_jishaku_environ(config_data.jishaku_config)

    bot = commands.Bot(
        command_prefix=config_data.bot_config.prefix,
        help_command=DefaultPaginatorHelp(),
        owner_ids=config_data.bot_config.owner_ids,
        self_bot=True,
    )


    bot.load_extension("jishaku")


    bot.run(config_data.bot_config.token, bot=False)


if __name__ == "__main__":
    main()
