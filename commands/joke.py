import pyjokes
from command import Command


class Joke(Command):
    def __init__(self, comm):
        super().__init__(comm)
        self.aliases = ["joke"]

    def _execute(self):
        return False, pyjokes.get_joke(), None
