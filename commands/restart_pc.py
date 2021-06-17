import ipaddress
import socket
import subprocess

from classes.command import Command
from utilities.settings import Settings


class RestartPc(Command):
    def __init__(self):
        super().__init__()
        self.aliases = [
            "Restart my PC",
            "Restart PC",
            "Restart my computer",
            "Restart computer",
            "Reboot my PC",
            "Reboot PC",
            "Reboot my computer",
            "Reboot computer",
        ]
        self.target = "pc"

    def _execute(self):
        subprocess.call("shutdown /r /t 10")
        return (
            False,
            f"OK. Restarting PC in just a moment.",
            None,
        )
