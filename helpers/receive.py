import websockets
import json


# Recieves the transcription input from assemblyai and you can do whatever you want with this input
async def receive(_ws):
    while True:
        try:
            result_str = await _ws.recv()
            result = json.loads(result_str)['text']

            if json.loads(result_str)['message_type'] == 'FinalTranscript':
                print(result)

        except websockets.exceptions.ConnectionClosedError as e:
            print(e)
            assert e.code == 4008
            break

        except Exception as e:
            print(e)
            assert False, "Not a websocket 4008 error"
