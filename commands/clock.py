import datetime

from classes.command import Command


class Clock(Command):
    def __init__(self):
        super().__init__()
        self.aliases = [
            "what's time is it?",
            "what time is it?",
        ]

    def _execute(self):
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        return (
            False,
            f"Sir, the time is {strTime}",
            None,
        )
