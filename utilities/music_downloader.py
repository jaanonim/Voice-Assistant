import os
import string
import threading
import time

import requests
from youtubesearchpython import *


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
        self.fetcher = None
        self.thread = None

        t = threading.Thread(name="getFether", target=self.get_fether)
        t.start()

    def get_fether(self):
        self.fetcher = StreamURLFetcher()

    def _start(self):
        if not self.thread:
            self.thread = threading.Thread(name="downloader", target=self.loop)
            self.thread.start()

    def get_id(self, name):
        try:
            data = VideosSearch(name, limit=1).result()["result"][0]
            return data["id"], self.format_title(data["title"])
        except:
            return None

    def get_file(self, id):
        for f in os.listdir("assets/music"):
            if f.startswith(id) and f.endswith(".webm"):
                return "assets/music/" + f
        return None

    def add_to_queue(self, id, title):
        while not self.fetcher:
            pass
        video = Video.get(f"https://www.youtube.com/watch?v={id}")
        url = self.fetcher.get(video, 251)
        self.queue.append((url, id, title))
        self._start()

    def loop(self):
        while True:
            if len(self.queue) > 0:
                url, id, title = self.queue[0]
                self.queue.pop(0)
                print(f"[DOWNLO] Start downloading '{id}' ...")
                r = requests.get(url, allow_redirects=True)
                open(f"assets/music/{id}{title}.webm", "wb").write(r.content)
                print(f"[DOWNLO] Done '{id}'")

    def format_title(self, title):
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        return "".join(c for c in title if c in valid_chars)
