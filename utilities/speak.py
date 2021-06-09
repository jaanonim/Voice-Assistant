import sys

import pyttsx3

text = str(sys.argv[1])
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

engine.say(text)
engine.runAndWait()
