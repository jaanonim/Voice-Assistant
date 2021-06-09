import requests
from command import Command


class Commit(Command):
    def __init__(self, comm):
        super().__init__(comm)
        self.aliases = ["commit"]

    def _execute(self):
        r = requests.get("http://whatthecommit.com/index.json")
        data = r.json()
        return False, data["commit_message"], None
