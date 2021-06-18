from subprocess import call

import simpleaudio as sa

from .settings import Settings


class Speaker:
    __instance = None

    @staticmethod
    def getInstance():
        if Speaker.__instance == None:
            Speaker()
        return Speaker.__instance

    def __init__(self):
        if Speaker.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Speaker.__instance = self

        self.wave_obj = {}
        self.outputVoice = Settings.getInstance().get("outputVoice")

    def speak(self, text):
        self.printMessage(text)
        if self.outputVoice:
            call(["python", "utilities/speak.py", str(text)])

    def printMessage(self, msg):
        print(f"[OUTPUT] {msg}")

    def notify(self):
        if not self.outputVoice:
            return
        if not self.wave_obj.get("notify"):
            self.wave_obj["notify"] = sa.WaveObject.from_wave_file(
                "assets/sounds/notification.wav"
            )

        self.wave_obj["notify"].play()

    def alarm(self):
        self.printMessage("Time's up!")
        if not self.outputVoice:
            return
        if not self.wave_obj.get("alarm"):
            self.wave_obj["alarm"] = sa.WaveObject.from_wave_file(
                "assets/sounds/alarm.wav"
            )

        self.wave_obj["alarm"].play()
