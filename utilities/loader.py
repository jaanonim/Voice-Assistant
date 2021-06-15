import importlib
import os
import re


def load_commands():
    commands = []
    for f in os.listdir("commands"):
        if f.endswith(".py"):
            f = str(f).replace(".py", "")
            commands.append(get_class("commands", f))
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