from loader import load_commands
from utilities.io import IO
from utilities.speech import Speaker

commands = None


def process_command(comm):
    global commands
    for c in commands:
        print(".", end="")
        obj = c(comm)
        if obj.check():
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
    IO(process_command).run()


if __name__ == "__main__":
    main()
