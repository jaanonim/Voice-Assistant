from classes.command import Command
from utilities.music_player import MusicPlayer


class Now(Command):
    def __init__(self):
        super().__init__()
        self.aliases = ["What's playing now"]

    def _execute(self):
        t = MusicPlayer.getInstance().title
        if t:
            return False, f"Now it's playing {t}", None
        return "Nothing is currently playing"
