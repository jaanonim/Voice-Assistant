from classes.command import Command


class Hello(Command):
    def __init__(self):
        super().__init__()
        self.aliases = ["hello", "hi", "good morning"]

    def _execute(self):
        return False, "Hello Sir!", None
