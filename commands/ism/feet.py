import requests
from classes.command import Command
from utilities.settings import Settings


class Feet(Command):
    def __init__(self):
        super().__init__()
        self.aliases = [
            "feed the fish",
            "feed fish",
            "food to fish",
            "food to the fish",
        ]

    def _execute(self):
        url = Settings.getInstance().get("ismaAdres")
        try:
            requests.get(f"{url}/karm")
        except:
            return False, "Something went wrong.", None
        return False, "OK. I'm feeding the fish.", None
