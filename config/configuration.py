import json


class Config(object):
    def __init__(self,config_path):
        self.filepath = config_path
        self._config = {}
        self.open()

    def open(self):
        f = open(self.filepath)
        self._config = json.load(f)

    def config(self):
        return self._config


if __name__ == "__main__":
    config = Config('../config.json').config()
    print(config)