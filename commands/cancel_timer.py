from classes.command import Command
from utilities.cache import Cache


class CancelTimer(Command):
    def __init__(self):
        super().__init__()
        self.aliases = [
            "Cancel timer",
            "Cancel all timer",
            "Cancel timers",
            "Cancel all timers",
        ]

    def _execute(self):

        data = Cache.getInstance().get("timers")
        if not data:
            return (
                False,
                f"Ther is not timers set",
                None,
            )
        for t in data:
            t.terminate()
        Cache.getInstance().set("timers", [])
        return (
            False,
            f"OK. All timers have been canceled.",
            None,
        )
