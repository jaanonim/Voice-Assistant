from command import Command


class SwitchPc(Command):
    def __init__(self):
        super().__init__()
        self.aliases = ["Turn {on_off|I did not hear turn on or off?} PC"]
        self.target = "pc"

    def _execute(self):
        return (
            False,
            f"OK. Turning {'on' if self.values['on_off'] else 'off' }.",
            None,
        )
