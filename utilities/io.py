from settings import Settings

from utilities.speech import Listener, Speaker


class IO:
    def __init__(self, func):
        self.func = func
        self.inputVoice = Settings.getInstance().get("inputVoice")

    def run(self):
        if self.inputVoice:
            Listener(self.func, None)
            while True:
                pass
        else:
            while True:
                inp = input("INPUT: ")
                if inp:
                    self.func(inp)
