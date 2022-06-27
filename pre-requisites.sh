#!/usr/bin/env bash

# Download the speechrecognition models and unzip them
if [ ! -d "./vosk-model-nl-spraakherkenning-0.6" ]
then
    wget https://alphacephei.com/vosk/models/vosk-model-nl-spraakherkenning-0.6.zip
    unzip vosk-model-nl-spraakherkenning-0.6.zip
    rm vosk-model-nl-spraakherkenning-0.6.zip
fi

# We need this library to be able to create the python wheel for pyaudio
dpkg -l | grep portaudio19-dev &> /dev/null
if [ $? -gt 0 ]
then
    sudo apt-get install portaudio19-dev -y
fi

# create our venv
if [ ! -d "./.venv" ]
then
    python3 -m venv .venv
    ./.venv/bin/pip install -r requirements.txt
fi

