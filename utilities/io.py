from settings import Settings

from .listener import Listener
from .speaker import Speaker


class IO:
    def __init__(self, func):
        self.func = func
        self.inputVoice = Settings.getInstance().get("inputVoice")

    def run(self):

        if self.inputVoice:
            Listener(self.func, Settings.getInstance().get("invocation")).setup()
            while True:
                pass
        else:
            l = Listener(self.func, None)
            while True:
                inp = input("INPUT: ")
                if inp:
                    l.proccess_command(inp, lambda: None)
