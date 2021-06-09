import sys
import threading
from subprocess import call

import pyttsx3
import speech_recognition as sr


class Listener:
    def __init__(self, process_func, invocation):
        self.process_func = process_func
        if invocation:
            self.invocation = invocation.lower()
        self.invocation = None
        self.active = False

        self.r = sr.Recognizer()
        self.mic = sr.Microphone()

        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)

        self.listen()

    def listen(self):
        print("Listening...")
        self.r.listen_in_background(self.mic, self.callback)

    def callback(self, r, audio):
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-us")
            print(f"User said: {query}\n")

        except Exception as e:
            print(f"Unable to Recognize your voice. {e}")
            return

        t = threading.Thread(
            target=self.proccess_command,
            args=(
                query.lower(),
                self.listen,
            ),
        )
        t.name = "processing command"
        t.start()
        sys.exit()

    def proccess_command(self, comm, callback):
        if self.active:
            self.active = self.process_func(comm)
        else:
            if self.invocation:
                if not self.invocation in comm:
                    return
                _, comm = comm.split(self.invocation, 1)

            comm = comm.strip()
            if comm:
                self.active = self.process_func(comm)
            else:
                self.active = True
        if self.active == None:
            self.active = False
        callback()


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

        self.engine = pyttsx3.init()
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[1].id)

    def speak(self, text):
        call(["py", "utilities\speak.py", text])
        # self.printMessage(text)
        # self.engine.say(text)
        # self.engine.runAndWait()

    def printMessage(self, msg):
        print(f"OUTPUT: {msg}")
