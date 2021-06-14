from subprocess import call

from settings import Settings


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

        self.outputVoice = Settings.getInstance().get("outputVoice")

    def speak(self, text):
        self.printMessage(text)
        if self.outputVoice:
            call(["python", "utilities\speak.py", str(text)])

    def printMessage(self, msg):
        print(f"OUTPUT: {msg}")
