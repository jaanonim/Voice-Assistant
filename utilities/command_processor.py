from loader import load_commands

from utilities.speech import Speaker


class CommandProcessor:
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

        print("Loading commands...")
        self.commands = load_commands()

    def process(self, comm):
        for c in self.commands:
            print(".", end="")
            obj = c()
            if obj.check(comm):
                print("")
                v, res, o = obj.execute()
                Speaker.getInstance().speak(res)
                if o:
                    return True, (o, obj)
                return v, None
        print("")
        return False, None
