from loader import load_commands
from utilities.speech import Listener, Speaker


def process_command(comm):
    for c in load_commands():
        obj = c(comm)
        if obj.check():
            v, res, _ = obj.execute()
            Speaker.getInstance().speak(res)
            return v
    return False


def main():
    Listener(process_command, None)
    while True:
        inp = input()
        if inp:
            process_command(inp)


if __name__ == "__main__":
    main()
