import ipaddress
import socket

from command import Command
from settings import Settings
from utilities.wake_on_lan import wake_up


class StartPc(Command):
    def __init__(self):
        super().__init__()
        self.aliases = [
            "Turn on my PC",
            "Turn on PC",
            "Start PC",
            "Turn on my Computer",
            "Turn on Computer",
            "Start Computer",
        ]

    def _execute(self):
        wake_up(Settings.getInstance().get("pcMacAdres"),Settings.getInstance().get("brodcastAdres"))
        return (
            False,
            f"OK. Turning on PC.",
            None,
        )
