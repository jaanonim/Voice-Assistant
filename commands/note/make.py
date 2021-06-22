from classes.command import Command
from utilities.settings import Settings


class Make(Command):
    def __init__(self):
        super().__init__()
        self.aliases = ["Note {name| }"]

    def _execute(self):
        Settings.getInstance().set("note", self.values["name"])
        return False, "OK. I'll make a note.", None
