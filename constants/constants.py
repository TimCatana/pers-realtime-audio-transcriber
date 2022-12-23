import pyaudio

AAI_REAL_TIME_TRANSCRIPTION_ENDPOINT = "wss://api.assemblyai.com/v2/realtime/ws?sample_rate=16000"
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 1600
