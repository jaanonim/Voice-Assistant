import random
import threading
import time

from ffpyplayer.player import MediaPlayer
from youtubesearchpython import Playlist

from .music_downloader import MusicDownloader
from .settings import Settings


class MusicPlayer:

    __instance = None

    @staticmethod
    def getInstance():
        if MusicPlayer.__instance == None:
            MusicPlayer()
        return MusicPlayer.__instance

    def __init__(self):

        if MusicPlayer.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            MusicPlayer.__instance = self

        self.queue = []
        self.player = None
        self._break = True
        self.id = None
        self.title = None
        self.volume = 0.1
        thread = threading.Thread(name="music", target=self.run)
        thread.start()

    def run(self):
        while True:
            if len(self.queue) > 0:
                self.id, self.title = self.queue[0]
                f_name = MusicDownloader.getInstance().get_file(self.id)
                while f_name == None:
                    f_name = MusicDownloader.getInstance().get_file(self.id)
                    time.sleep(1)
                self.player = MediaPlayer(f_name, volume=self.volume)

                val = ""
                while val != "eof" and self._break:
                    print(self._break)
                    frame, val = self.player.get_frame()
                    if val != "eof" and frame is not None:
                        img, t = frame
                if len(self.queue) > 0:
                    self.queue.pop(0)
                    self.reset()
            else:
                self.reset()

    def reset(self):
        del self.player
        self._break = True
        self.player = None
        self.id = None
        self.title = None

    def add_to_queue(self, id, title):
        self.queue.append((id, title))
        if not MusicDownloader.getInstance().get_file(id):
            MusicDownloader.getInstance().add_to_queue(id, title)
            return False
        return True

    def pause(self):
        if self.player:
            if not self.player.get_pause():
                self.player.toggle_pause()
                return "OK"
            else:
                return "The music is already paused"
        return "Nothing is currently playing"

    def play(self):
        if self.player:
            if self.player.get_pause():
                self.player.toggle_pause()
                return "OK"
            else:
                return "The music is already playing"
        return "Nothing is currently playing"

    def stop(self):
        if self.player:
            self._break = False
            self.queue = []
            return "OK"
        return "Nothing is currently playing"

    def set_volume(self, v):
        self.volume = v / 100
        if self.player:
            self.player.set_volume(self.volume)
        return f"OK stetting volume to {self.volume}"

    def random(self):
        if len(self.queue) > 0:
            random.shuffle(self.queue)
            return "OK"
        return "There is nothing in the queue."

    def skip(self):
        if self.player:
            self._break = False
            return "OK"
        return "Nothing is currently playing"

    def my_playlist(self):
        videos = Playlist.get(Settings.getInstance().get("playlistUrl"))["videos"]
        random.shuffle(videos)
        t = threading.Thread(name="playlist", target=self._my_playlist, args=(videos,))
        t.start()

    def _my_playlist(self, videos):
        for v in videos:
            self.add_to_queue(
                v["id"], MusicDownloader.getInstance().format_title(v["title"])
            )
