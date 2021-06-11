import pyjokes
from command import Command


class Joke(Command):
    def __init__(self):
        super().__init__()
        self.aliases = ["joke"]

    def _execute(self):
        return False, pyjokes.get_joke(), None
