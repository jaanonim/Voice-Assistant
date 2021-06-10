from command import Command


class SwitchPc(Command):
    def __init__(self, comm):
        super().__init__(comm)
        self.aliases = ["Turn {on_off|I did not hear turn on or off?} PC"]

    def _execute(self):
        return False, f"OK. Turning {'on' if self.values[0] else 'off' }.", None
