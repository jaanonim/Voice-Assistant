import winshell
from classes.command import Command


class Bin(Command):
    def __init__(self):
        super().__init__()
        self.aliases = [
            "empty recycle bin",
            "empty bin",
        ]
        self.target = "pc"

    def _execute(self):
        try:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        except:
            return (
                False,
                f"Something went wrong.",
                None,
            )
        return (
            False,
            f"Recycle Bin Recycled.",
            None,
        )
