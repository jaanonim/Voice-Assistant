import ipaddress
import socket
import subprocess

from classes.command import Command
from utilities.settings import Settings


class Shutdown(Command):
    def __init__(self):
        super().__init__()
        self.aliases = [
            "Turn off my PC",
            "Turn off PC",
            "Shutdown PC",
            "Turn off my computer",
            "Turn off computer",
            "Shutdown computer",
        ]
        self.target = "pc"

    def _execute(self):
        subprocess.call("shutdown /s /t 10")
        return (
            False,
            f"OK. Turning off PC in just a moment.",
            None,
        )
