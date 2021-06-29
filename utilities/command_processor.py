from .loader import load_commands
from .speaker import Speaker


class CommandProcessor:
    __instance = None

    @staticmethod
    def getInstance():
        if CommandProcessor.__instance == None:
            CommandProcessor()
        return CommandProcessor.__instance

    def __init__(self):

        if CommandProcessor.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            CommandProcessor.__instance = self

        print("[ENGINE] Loading commands...")
        self.commands = load_commands()

    def process(self, comm):
        print("[ENGINE] ", end="")
        for item in self.commands:
            c, url = item
            print(".", end="")
            if c is None:
                print("[ENGINE] Sothing went wrong when command was imported!")
                continue
            obj = c()
            if obj.check(comm):
                print("")
                v, res, o = obj.execute()
                Speaker.getInstance().speak(res)
                if o:
                    return True, (o, obj)
                return v, None
        print("")
        Speaker.getInstance().speak("I didn't understend")
        return False, None
