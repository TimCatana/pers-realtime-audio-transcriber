import websockets
import asyncio
import base64
import json
from constants.constants import *
from constants.api_secrets import API_KEY_ASSEMBLYAI
from helpers.send import send
from helpers.receive import receive


# asyncronously transcribe input and print it to console.
async def sendReceive(stream):
    print(
        f'Connecting websockets to url ${AAI_REAL_TIME_TRANSCRIPTION_ENDPOINT}')

    async with websockets.connect(
        AAI_REAL_TIME_TRANSCRIPTION_ENDPOINT,
        extra_headers=(("Authorization", API_KEY_ASSEMBLYAI),),
        ping_interval=5,
        ping_timeout=20
    ) as _ws:
        await asyncio.sleep(0.1)
        print("receiving session begins... ")

        sessionBegins = await _ws.recv()
        print(sessionBegins)
        print("sending messages...")

        send_result, receive_result = await asyncio.gather(send(_ws, stream), receive(_ws))
