import os
import sys
import threading
from subprocess import call

import pyttsx3
import simpleaudio as sa
import speech_recognition as sr
from loader import convert_to_snake_case
from settings import Settings


class Listener:
    def __init__(self, process_func, invocation):
        self.process_func = process_func
        self.invocation = None
        if invocation:
            self.invocation = invocation.lower()
        self.inputVoice = Settings.getInstance().get("inputVoice")
        self.active = False
        self.command = None
        self.wave_obj = None

    def setup(self):
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
            if self.command:
                atr, com = self.command
                v = atr.get_value(comm)
                if v:
                    com.values[convert_to_snake_case(atr.__name__)] = v
                    v, res, o = com.exec_target()
                    Speaker.getInstance().speak(res)
                    self.active = False
                    self.command = False
                    callback()
                    return
                else:
                    self.active = False
                    self.command = False
                    callback()
                    return
            self.active, self.command = self.process_func(comm)
        else:
            if self.invocation:
                if not self.invocation in comm:
                    callback()
                    return
                _, comm = comm.split(self.invocation, 1)

            comm = comm.strip()
            if comm:
                self.active, self.command = self.process_func(comm)
            else:
                self.notify()
                self.active = True
        if self.active == None:
            self.active = False
        if self.command:
            self.notify()
        callback()

    def notify(self):
        if not self.inputVoice:
            return
        if not self.wave_obj:
            self.wave_obj = sa.WaveObject.from_wave_file(
                "assets/sounds/notification.wav"
            )

        self.wave_obj.play()


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
            call(["py", "utilities\speak.py", str(text)])

    def printMessage(self, msg):
        print(f"OUTPUT: {msg}")
