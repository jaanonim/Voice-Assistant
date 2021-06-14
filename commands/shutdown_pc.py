import ipaddress
import socket
import subprocess

from command import Command
from settings import Settings
from utilities.wake_on_lan import wake_up


class StartPc(Command):
    def __init__(self):
        super().__init__()
        self.aliases = [
            "Turn off my PC",
            "Turn off PC",
            "Start PC",
            "Shutdown off my computer",
            "Turn off computer",
            "Shutdown computer",
        ]

    def _execute(self):
        subprocess.call("shutdown /s /t 10")
        return (
            False,
            f"OK. Turning off PC in just a moment.",
            None,
        )
