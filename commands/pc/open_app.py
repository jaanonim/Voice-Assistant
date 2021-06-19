import webbrowser

import winapps
from classes.command import Command


class OpenApp(Command):
    def __init__(self):
        super().__init__()
        self.aliases = [
            "open app {name|what app should I open?}",
            "open application {name|what application should I open?}",
            "open program {name|what program should I open?}",
            "start app {name|what app should I open?}",
            "start application {name|what application should I open?}",
            "start program {name|what program should I open?}",
        ]
        self.target = "pc"

    def _execute(self):
        #TODO: Implement search in win - good luck
        return False, "Not implemented.", None
        n = self.values.get("name")
        print(n)
        ok = False
        for app in winapps.search_installed(n):
            ok = True
            print(app)
            break
        if ok:
            return False, f"OK. Opening {n}", None
        else:
            return False, f"Not found app {n}.", None
