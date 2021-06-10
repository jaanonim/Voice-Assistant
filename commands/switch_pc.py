from command import Command


class SwitchPc(Command):
    def __init__(self, comm):
        super().__init__(comm)
        self.aliases = ["Turn {on_off} PC"]

    def _execute(self):
        return False, self.values[0], None
