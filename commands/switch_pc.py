from command import Command


class SwitchPc(Command):
    def __init__(self, comm):
        super().__init__(comm)
        self.aliases = ["Turn on PC"]

    def _execute(self):
        return False, "eee", None
