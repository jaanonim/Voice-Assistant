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
            d = MusicDownloader.getInstance().get_id(to_play)
            if d:
                id, title = d
                if MusicPlayer.getInstance().add_to_queue(id, title):
                    return False, "OK", None
                else:
                    return (
                        False,
                        "OK. Please wait a minute, I need to download this song.",
                        None,
                    )
            else:
                return False, "Track not found", None
        else:
            return False, MusicPlayer.getInstance().play(), None
