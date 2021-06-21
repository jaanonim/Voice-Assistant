from classes.command import Command
from utilities.music_player import MusicPlayer


class Skip(Command):
    def __init__(self):
        super().__init__()
        self.aliases = ["skip", "next"]

    def _execute(self):
        return False, MusicPlayer.getInstance().skip(), None
