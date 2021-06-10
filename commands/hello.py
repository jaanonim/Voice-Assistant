from command import Command


class Hello(Command):
    def __init__(self, comm):
        super().__init__(comm)
        self.aliases = ["hello {xxd} can", "hi", "gut morning"]

    def _execute(self):
        return False, "Hello Sir!", None
