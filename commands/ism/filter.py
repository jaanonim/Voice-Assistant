import requests
from classes.command import Command
from utilities.settings import Settings


class Filter(Command):
    def __init__(self):
        super().__init__()
        self.aliases = [
            "Turn {on_off|I did not hear turn on or off?} filter",
            "Turn {on_off|I did not hear turn on or off?} the filter",
        ]

    def _execute(self):
        url = Settings.getInstance().get("ismaAdres")

        if self.values["on_off"]:
            url += "/onp2"
        else:
            url += "/offp2"

        try:
            requests.get(url)
        except:
            return False, "Something went wrong.", None
        return (
            False,
            f"OK. I turn {'on' if self.values['on_off'] else 'off'} the filter",
            None,
        )
