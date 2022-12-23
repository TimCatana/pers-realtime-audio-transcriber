# https://www.youtube.com/watch?v=5LJFK7eOC20&t=111s
# https://github.com/misraturp/Real-time-transcription-from-microphone/blob/main/sr_in_streamlit.py

import pyaudio
import asyncio
from constants.constants import *
from helpers.sendRecieve import sendReceive


# main
if __name__ == "__main__":
    p = pyaudio.PyAudio()

    # starts recording
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=FRAMES_PER_BUFFER
    )
    asyncio.run(sendReceive(stream))
