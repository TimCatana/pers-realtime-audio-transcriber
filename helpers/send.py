import websockets
import asyncio
import base64
import json
from constants.constants import *


# send the audio to assembly ai for transcription via websockets

async def send(_ws, stream):
    while True:
        try:
            data = stream.read(FRAMES_PER_BUFFER)
            data = base64.b64encode(data).decode("utf-8")
            json_data = json.dumps({"audio_data": str(data)})
            await _ws.send(json_data)

        except websockets.exceptions.ConnectionClosedError as e:
            print(e)
            assert e.code == 4008
            break

        except Exception as e:
            print(e)
            assert False, "Not a websocket 4008 error"

        await asyncio.sleep(0.01)
