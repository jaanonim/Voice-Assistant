import ipaddress
import socket
import subprocess

from classes.command import Command
from utilities.settings import Settings


class HibernatePc(Command):
    def __init__(self):
        super().__init__()
        self.aliases = [
            "Hibernate my PC",
            "Hibernate PC",
            "Hibernate my computer",
            "Hibernate computer",
        ]
        self.target = "pc"

    def _execute(self):
        subprocess.call("shutdown /h")
        return (
            False,
            f"OK. Hibernating PC in just a moment.",
            None,
        )
