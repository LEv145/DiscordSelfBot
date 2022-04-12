from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BaseConfig():
    bot_config: BotConfig
    jishaku_config: JishakuConfig | None = None


@dataclass
class BotConfig():
    token: str
    owner_ids: list[int]
    prefix: str


@dataclass
class JishakuConfig():  # TODO: Naming
    retain: bool | None = None
    no_underscore_prefix: bool | None = True
    force_paginator: bool | None = False
    no_dm_traceback: bool | None = None
    always_dm_traceback: bool | None = None
    use_ansi_always: bool | None = None
    use_ansi_never: bool | None = None
