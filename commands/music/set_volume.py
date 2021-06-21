from classes.command import Command
from utilities.music_player import MusicPlayer


class SetVolume(Command):
    def __init__(self):
        super().__init__()
        self.aliases = ["set volume {volume|What volume to set?}"]

    def _execute(self):
        return False, MusicPlayer.getInstance().set_volume(self.values["volume"]), None
