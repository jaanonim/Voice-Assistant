import os
import sys
import threading

import pyttsx3
import speech_recognition as sr

from .command_processor import CommandProcessor
from .loader import convert_to_snake_case
from .settings import Settings
from .speaker import Speaker


class Listener:
    def __init__(self, invocation):
        self.invocation = None
        if invocation:
            self.invocation = invocation.lower()
        self.inputVoice = Settings.getInstance().get("inputVoice")
        self.active = False
        self.command = None

    def setup(self):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()

        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)
        self.listen()

    def listen(self):
        print("[ENGINE] Listening...")
        self.r.listen_in_background(self.mic, self.callback)

    def callback(self, r, audio):
        try:
            print("[ENGINE] Recognizing...")
            query = r.recognize_google(audio, language="en-us")
            print(f"[ENGINE] User said: {query}\n")

        except Exception as e:
            print(f"[ENGINE] Unable to Recognize your voice. {e}")
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
            self.active, self.command = CommandProcessor.getInstance().process(comm)
        else:
            if self.invocation:
                if not self.invocation in comm:
                    callback()
                    return
                _, comm = comm.split(self.invocation, 1)

            comm = comm.strip()
            if comm:
                self.active, self.command = CommandProcessor.getInstance().process(comm)
            else:
                Speaker.getInstance().notify()
                self.active = True
        if self.active == None:
            self.active = False
        if self.command:
            Speaker.getInstance().notify()
        callback()
