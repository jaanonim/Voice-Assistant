import importlib
import os


def load_commands():
    commands = []
    for f in os.listdir("commands"):
        if f.endswith(".py"):
            f = str(f).replace(".py", "")
            name = "".join(x for x in f.title() if not x == "_")
            commands.append(getattr(importlib.import_module(f"commands.{f}"), name))
    return commands
