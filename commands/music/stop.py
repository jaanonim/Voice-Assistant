from classes.command import Command
from utilities.music_player import MusicPlayer


class Stop(Command):
    def __init__(self):
        super().__init__()
        self.aliases = ["stop playing", "stop music"]

    def _execute(self):
        return False, MusicPlayer.getInstance().stop(), None
