from .listener import Listener
from .settings import Settings
from .speaker import Speaker


class IO:
    def __init__(self):
        self.inputVoice = Settings.getInstance().get("inputVoice")

    def run(self):

        if self.inputVoice:
            Listener(Settings.getInstance().get("invocation")).setup()
            while True:
                pass
        else:
            l = Listener(None)
            while True:
                inp = input("[INPUT] > ")
                if inp:
                    l.proccess_command(inp, lambda: None)
