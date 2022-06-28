"""
Dit script is een test met Vlaamse spraakherkenning.

Indien men het woord "print" zegt gevolgd door een cijfer, dan wordt de zin n
keer geprint.
"""
from vosk import Model, KaldiRecognizer
import pyaudio
import os
import sys

tekst_cijfers = {
    "een": 1,
    "twee": 2,
    "drie": 3,
    "vier": 4,
    "vijf": 5
}

model = Model("/".join([os.getcwd(), "vosk-model-nl-spraakherkenning-0.6/"]))
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    try:
        data = stream.read(4096)
    
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            print(text[14:-3])
            for k, v in tekst_cijfers.items():
                if "print" in text and k in text:
                    for i in range(v):
                        print(text[14:-3])
    except KeyboardInterrupt:
        if input("Are you sure that you want to exit? [y/n] ").lower() == "y":
            sys.exit()

