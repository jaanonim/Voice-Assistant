import threading
import time

from classes.command import Command
from utilities.speaker import Speaker


class Timer(Command):
    def __init__(self):
        super().__init__()
        self.aliases = [
            "Set timer for {time|how long should I set the timer?}",
        ]

    def _execute(self):
        v, s = self.values["time"]
        thread = threading.Thread(name="timer", target=self.setTimer, args=(v,))
        thread.start()
        return (
            False,
            f"The timer is set to {s}",
            None,
        )

    def setTimer(self, v):
        time.sleep(v)
        Speaker.getInstance().alarm()
