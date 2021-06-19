import importlib
import os
import re

ignore_dirs = ["__pycache__"]


def load_commands():
    commands = []
    for root, dirs, files in os.walk("commands"):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        if not ignore_dirs in dirs:
            for name in files:
                if name.endswith(".py"):
                    name = name.replace(".py", "")
                    commands.append(
                        get_class(root.replace("\\", ".").replace("/", "."), name)
                    )

    return commands


def convert_to_pascal_case(text):
    return "".join(x for x in text.title() if not x == "_")


def convert_to_snake_case(text):
    return re.sub(r"(?<!^)(?=[A-Z])", "_", text).lower()


def get_class(dir, name):
    n = convert_to_pascal_case(name)
    try:
        return getattr(importlib.import_module(f"{dir}.{name}"), n)
    except:
        return None
