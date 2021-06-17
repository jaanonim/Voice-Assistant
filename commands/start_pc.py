import ipaddress
import socket

import wakeonlan
from classes.command import Command
from utilities.settings import Settings


class StartPc(Command):
    def __init__(self):
        super().__init__()
        self.aliases = [
            "Turn on my PC",
            "Turn on PC",
            "Start my PC",
            "Start PC",
            "Turn on my Computer",
            "Turn on Computer",
            "Start my Computer",
            "Start Computer",
        ]

    def _execute(self):
        try:
            wakeonlan.send_magic_packet(
                Settings.getInstance().get("pcMacAdres"),
            )
            return (
                False,
                f"OK. Turning on PC.",
                None,
            )
        except Exception as e:
            return (
                False,
                str(e),
                None,
            )
