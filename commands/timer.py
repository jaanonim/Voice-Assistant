import multiprocessing
import time

from classes.command import Command
from utilities.cache import Cache
from utilities.speaker import Speaker


class Timer(Command):
    def __init__(self):
        super().__init__()
        self.aliases = [
            "Set timer for {time|how long should I set the timer?}",
        ]

    def _execute(self):
        v, s = self.values["time"]
        p = multiprocessing.Process(name="timer", target=self.setTimer, args=(v,))
        p.start()
        data = Cache.getInstance().get("timers")
        if not data:
            data = []
        data.append(p)
        Cache.getInstance().set("timers", data)
        return (
            False,
            f"The timer is set to {s}",
            None,
        )

    def setTimer(self, v):
        time.sleep(v)
        Speaker.getInstance().alarm()
