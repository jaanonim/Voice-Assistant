import time

import keyboard
import psutil
from classes.command import Command


class OpenApp(Command):
    def __init__(self):
        super().__init__()
        self.aliases = [
            "open up {name|what app should I open?}",
            "open app {name|what app should I open?}",
            "open application {name|what application should I open?}",
            "start app {name|what app should I open?}",
            "start application {name|what application should I open?}",
            "start program {name|what program should I open?}",
        ]
        self.target = "pc"

    def _execute(self):
        n = self.values.get("name")
        if self.is_power_launcher_running():
            keyboard.press_and_release("alt+space")
            time.sleep(0.1)
            keyboard.press_and_release("backspace")
            keyboard.write(n)
            time.sleep(0.1)
            keyboard.press_and_release("enter")

            return False, f"OK. Opening {n}", None

        return False, "To open apps you need to have running Power Launcher.", None

    def is_power_launcher_running(self):
        for p in psutil.process_iter():
            if "PowerLauncher.exe" == p.name():
                return True
        return False
