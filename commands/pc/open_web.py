import webbrowser

from classes.command import Command


class OpenWeb(Command):
    def __init__(self):
        super().__init__()
        self.aliases = [
            "open website {name|what webpage should I open?}",
            "open web {name|what webpage should I open?}",
        ]
        self.target = "pc"

    def _execute(self):
        n = self.values.get("name")
        webbrowser.open(f"www.{n}")
        return False, f"OK. Opening {n}", None
