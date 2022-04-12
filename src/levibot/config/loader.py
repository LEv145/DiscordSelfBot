import toml
from pathlib import Path

from .model import BaseConfig, BotConfig, JishakuConfig


class ConfigLoader():
    def __init__(self, path: Path):
        self._path = path

    def load(self) -> BaseConfig:
        with open(self._path) as fp:
            config_raw_data = toml.load(fp)

        try:
            bot_raw_config = config_raw_data["bot"]
            config = BaseConfig(
                bot_config=BotConfig(
                    token=bot_raw_config["token"],
                    owner_ids=bot_raw_config["owner_ids"],
                    prefix=bot_raw_config["prefix"],
                )
            )
        except KeyError as exception:
            raise InvalidConfig() from exception

        jishaku_raw_config = config_raw_data.get("jishaku")
        if jishaku_raw_config is not None:
            config.jishaku_config = JishakuConfig(
                retain=jishaku_raw_config.get("retain"),
                no_underscore_prefix=jishaku_raw_config.get("no_underscore_prefix"),
                force_paginator=jishaku_raw_config.get("force_paginator"),
                no_dm_traceback=jishaku_raw_config.get("no_dm_traceback"),
                always_dm_traceback=jishaku_raw_config.get("always_dm_traceback"),
                use_ansi_always=jishaku_raw_config.get("use_ansi_always"),
                use_ansi_never=jishaku_raw_config.get("use_ansi_never"),
            )

        return config


class InvalidConfig(Exception):
    ...
