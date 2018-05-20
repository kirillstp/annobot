import json

FILEPATH = 'config.json'

class Config(object):
    def __init__(self):
        self.filepath = self.FILEPATH
        self._config = {}
        self.open()

    def open():
        f = open(self.filepath)
        self._config = json.load(f)

    @config.getter
    def config(self):
        return self._config