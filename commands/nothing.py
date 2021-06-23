from classes.command import Command


class Nothing(Command):
    def __init__(self):
        super().__init__()
        self.aliases = ["nothing", "cancel", "never mind"]

    def _execute(self):
        return False, "", None
