from classes.command import Command
from utilities.music_player import MusicPlayer


class Shuffle(Command):
    def __init__(self):
        super().__init__()
        self.aliases = ["random q", "shuffle q"]

    def _execute(self):
        return False, MusicPlayer.getInstance().random(), None
