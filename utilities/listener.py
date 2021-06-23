import os
import struct
import sys
import threading

import pvporcupine
import pyaudio
import pyttsx3
import speech_recognition as sr

from .command_processor import CommandProcessor
from .loader import convert_to_snake_case
from .music_player import MusicPlayer
from .settings import Settings
from .speaker import Speaker


class Listener:
    def __init__(self):
        self.inputVoice = Settings.getInstance().get("inputVoice")
        self.keywords = Settings.getInstance().get("invocation")
        self.active = False
        self.command = None

    def setup(self):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()

        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)

        if not self.keywords:
            self.listen()
        else:
            self.wait_for_awake()

    def wait_for_awake(self):

        porcupine = pvporcupine.create(keywords=self.keywords)

        pa = pyaudio.PyAudio()

        audio_stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length,
        )

        last = not self.active
        while True:
            if last and not self.active:
                print("[ENGINE] Ready")
                last = self.active
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0 and (not self.active):
                Speaker.getInstance().notify()
                self.listen()

    def listen(self):
        print("[ENGINE] Listening...")
        MusicPlayer.getInstance().pause()
        self.active = True
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
            name="processing command",
            target=self.proccess_command,
            args=(
                query.lower(),
                self.listen,
            ),
        )
        t.start()
        sys.exit()

    def proccess_command(self, comm, callback):
        if self.command:
            atr, com = self.command
            v = atr.get_value(comm)
            if v:
                com.values[convert_to_snake_case(atr.__name__)] = v
                v, res, o = com.exec_target()
                Speaker.getInstance().speak(res)
                self.active = False
                self.command = False
                MusicPlayer.getInstance().play()
                return
            else:
                self.active = False
                self.command = False
                MusicPlayer.getInstance().play()
                return
        self.active, self.command = CommandProcessor.getInstance().process(comm)
        if self.command:
            Speaker.getInstance().notify()
        if self.active or self.keywords is None:
            callback()
        MusicPlayer.getInstance().play()
