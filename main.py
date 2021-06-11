from loader import load_commands
from network.client import Client
from network.server import Server
from settings import Settings
from utilities.io import IO
from utilities.speech import Speaker

commands = None


def process_command(comm):
    global commands
    for c in commands:
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


def main():
    global commands
    print("Loading commands...")
    commands = load_commands()
    if Settings.getInstance().get("isClient"):
        Client(commands)
    else:
        Server.getInstance()
        IO(process_command).run()


if __name__ == "__main__":
    main()
