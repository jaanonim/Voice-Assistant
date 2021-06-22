from classes.command import Command


class LoremIpsum(Command):
    def __init__(self):
        super().__init__()
        self.aliases = ["lorem ipsum"]

    def _execute(self):
        return (
            False,
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis in posuere nulla. Curabitur sit amet congue tellus. Sed a lacus ut elit tincidunt mattis ac porta lorem. Vivamus nisi urna, accumsan eget nisi sit amet, fringilla venenatis eros.",
            None,
        )
