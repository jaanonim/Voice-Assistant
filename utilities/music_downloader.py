import os
import string
import threading

import requests
from youtubesearchpython import *

valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)


class MusicDownloader:
    __instance = None

    @staticmethod
    def getInstance():
        if MusicDownloader.__instance == None:
            MusicDownloader()
        return MusicDownloader.__instance

    def __init__(self):

        if MusicDownloader.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            MusicDownloader.__instance = self

        self.queue = []
        self.fetcher = StreamURLFetcher()
        thread = threading.Thread(name="downloader", target=self.loop)
        thread.start()

    def get_id(self, name):
        data = VideosSearch(name, limit=1).result()["result"][0]
        id = data["id"]
        title = data["title"]
        title = "".join(c for c in title if c in valid_chars)
        return id, title

    def get_file(self, id, title):
        for f in os.listdir("assets/music"):
            if f.startswith(id) and f.endswith(".webm"):
                return "assets/music/"+f
        self.add_to_queue(id, title)
        return None

    def add_to_queue(self, id, title):
        video = Video.get(f"https://www.youtube.com/watch?v={id}")
        url = self.fetcher.get(video, 251)
        self.queue.append((url, id, title))

    def loop(self):
        while True:
            if len(self.queue) > 0:
                url, id, title = self.queue[0]
                self.queue.pop(0)
                r = requests.get(url, allow_redirects=True)
                open(f"assets/music/{id}{title}.webm", "wb").write(r.content)
