from classes.command import Command
from utilities.settings import Settings


class Read(Command):
    def __init__(self):
        super().__init__()
        self.aliases = ["read me my note", "read my note"]

    def _execute(self):
        note = Settings.getInstance().get("note")
        return False, f"OK. This is your note. {note}", None
