from classes.command import Command
from utilities.music_downloader import MusicDownloader
from utilities.music_player import MusicPlayer


class Play(Command):
    def __init__(self):
        super().__init__()
        self.aliases = ["play {name| }", "play"]

    def _execute(self):
        to_play = self.values.get("name")
        if to_play:
            id, title = MusicDownloader.getInstance().get_id(to_play)
            MusicPlayer.getInstance().addToQueue(id, title)
            return False, "OK", None
        else:
            return False, MusicPlayer.getInstance().play(), None
