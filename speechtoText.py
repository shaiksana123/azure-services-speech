# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# -------------------------------------------------------------------------

import azure.cognitiveservices.speech as speechsdk
import threading
from google.colab import files

# Enter your Azure credentials here
speech_key = "your Api Key"
endpoint_url = "https://24691a32n8-8780-resource.cognitiveservices.azure.com/"

# Configure Azure Speech
speech_config = speechsdk.SpeechConfig(
    subscription=speech_key,
    endpoint=endpoint_url
)

speech_config.speech_recognition_language = "en-US"

# Upload audio file
print("Upload your audio file:")
uploaded = files.upload()

audio_file = next(iter(uploaded.keys()))

# Configure audio input
audio_config = speechsdk.audio.AudioConfig(
    filename=audio_file
)

# Create speech recognizer
speech_recognizer = speechsdk.SpeechRecognizer(
    speech_config=speech_config,
    audio_config=audio_config
)

# Store recognized text
recognized_text = []

# Event handlers
def recognized_handler(evt):
    if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
        recognized_text.append(evt.result.text)
        print("Recognized:", evt.result.text)

def recognizing_handler(evt):
    if evt.result.text:
        print("Recognizing:", evt.result.text)

# Completion event
stop_event = threading.Event()

speech_recognizer.session_stopped.connect(
    lambda evt: stop_event.set()
)

speech_recognizer.canceled.connect(
    lambda evt: stop_event.set()
)

# Connect event handlers
speech_recognizer.recognized.connect(recognized_handler)
speech_recognizer.recognizing.connect(recognizing_handler)

# Start recognition
print("Speech recognition started...")
speech_recognizer.start_continuous_recognition()

# Wait for completion
stop_event.wait()

# Stop recognition
speech_recognizer.stop_continuous_recognition()

# Print transcript
print("\nFinal Transcript:")
print(" ".join(recognized_text))