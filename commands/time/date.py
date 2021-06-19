import datetime

from classes.command import Command


class Date(Command):
    def __init__(self):
        super().__init__()
        self.aliases = [
            "what's day is today?",
            "what day is today?",
        ]

    def _execute(self):
        strTime = datetime.datetime.now().strftime("%A, %d-%B-%Y")
        return (
            False,
            f"Sir, today is {strTime}",
            None,
        )
