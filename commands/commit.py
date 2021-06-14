import requests
from classes.command import Command


class Commit(Command):
    def __init__(self):
        super().__init__()
        self.aliases = ["commit"]

    def _execute(self):
        r = requests.get("http://whatthecommit.com/index.json")
        data = r.json()
        return False, data["commit_message"], None
