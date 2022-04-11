import toml
from pathlib import Path

from .model import ConfigModel


class ConfigLoader():
    def __init__(self, path: Path):
        self._path = path

    def load(self) -> ConfigModel:
        with open(self._path) as fp:
            config_raw_data = toml.load(fp)

        try:
            return ConfigModel(
                token=config_raw_data["bot"]["token"],
                owner_ids=config_raw_data["bot"]["owner_ids"],
            )
        except KeyError as exception:
            raise InvalidConfig() from exception


class InvalidConfig(Exception):
    ...
