import toml
from pathlib import Path

from .model import ConfigModel


class ConfigLoader():
    def __init__(self, path: Path):
        self._path = path

    def load(self) -> ConfigModel:
        with open(self._path) as fp:
            data = toml.load(fp)

        return ConfigModel(
            token=data["bot"]["token"],
        )
