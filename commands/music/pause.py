from classes.command import Command
from utilities.music_player import MusicPlayer


class Pause(Command):
    def __init__(self):
        super().__init__()
        self.aliases = ["pause"]

    def _execute(self):
        return False, MusicPlayer.getInstance().pause(), None
