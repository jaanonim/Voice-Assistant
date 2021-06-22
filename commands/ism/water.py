import requests
from classes.command import Command
from utilities.settings import Settings


class Water(Command):
    def __init__(self):
        super().__init__()
        self.aliases = [
            "water plants",
            "water flowers",
            "water the plants",
            "water the flowers",
        ]

    def _execute(self):
        url = Settings.getInstance().get("ismpAdres")
        try:
            requests.get(f"{url}/podlej")
        except:
            return False, "Something went wrong.", None
        return False, "OK. I water the plants.", None
