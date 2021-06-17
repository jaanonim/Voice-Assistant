import ipaddress
import socket
import subprocess

from classes.command import Command
from utilities.settings import Settings


class LogOffPc(Command):
    def __init__(self):
        super().__init__()
        self.aliases = [
            "Log off my PC",
            "Log off PC",
            "Log off my computer",
            "Log off computer",
            "Sign out my PC",
            "Sign out PC",
            "Sign out my computer",
            "Sign out computer",
        ]
        self.target = "pc"

    def _execute(self):
        subprocess.call("shutdown /l")
        return (
            False,
            f"OK. Log off PC in just a moment.",
            None,
        )
