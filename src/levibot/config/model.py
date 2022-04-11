from dataclasses import dataclass


@dataclass
class ConfigModel():
    token: str
    owner_ids: list[int]
    prefix: str
