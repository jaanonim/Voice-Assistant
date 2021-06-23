from classes.command import Command


class Coffe(Command):
    def __init__(self):
        super().__init__()
        self.aliases = ["Make me coffe", "Make me a coffe", "Make coffe"]

    def _execute(self):
        return False, "Sir, You don't like coffe.", None
