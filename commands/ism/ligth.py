import requests
from classes.command import Command
from utilities.settings import Settings


class Ligth(Command):
    def __init__(self):
        super().__init__()
        self.aliases = [
            "Turn {on_off|I did not hear turn on or off?} ligth",
            "Turn {on_off|I did not hear turn on or off?} the ligth",
        ]

    def _execute(self):
        url = Settings.getInstance().get("ismaAdres")

        if self.values["on_off"]:
            url += "/onp1"
        else:
            url += "/offp1"

        try:
            requests.get(url)
        except:
            return False, "Something went wrong.", None
        return (
            False,
            f"OK. I turn {'on' if self.values['on_off'] else 'off'} the ligth",
            None,
        )
