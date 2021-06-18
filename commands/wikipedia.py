from classes.command import Command

import wikipedia


class Wikipedia(Command):
    def __init__(self):
        super().__init__()
        self.aliases = [
            "wkipedia {name|What should I look for}",
            "what is {name|What should I look for}",
        ]

    def _execute(self):
        try:
            results = wikipedia.summary(self.values["name"], sentences=3)
            return False, f"According to Wikipedia: {results}", None
        except Exception as e:
            return (
                False,
                str(e),
                None,
            )
