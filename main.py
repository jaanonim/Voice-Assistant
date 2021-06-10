from loader import load_commands
from utilities.io import IO
from utilities.speech import Speaker


def process_command(comm):
    for c in load_commands():
        obj = c(comm)
        if obj.check():
            v, res, _ = obj.execute()
            Speaker.getInstance().speak(res)
            return v
    return False


def main():
    IO(process_command).run()


if __name__ == "__main__":
    main()
