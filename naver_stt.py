#stt
import requests
import pyaudio
import wave

import re


def main_stt():
    client_id = '728wa0ida5'
    client_secret = '4t9cpdUSI3UlCpXAKn8IEH0pXpiWBjkj8RtzhkR5'
    lang = 'Kor'
    url = 'https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=' + lang

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Start to record the audio.")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording is finished.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    data = open('output.wav', 'rb')

    headers = {
        'X-NCP-APIGW-API-KEY-ID': client_id,
        'X-NCP-APIGW-API-KEY': client_secret,
        'Content-Type': 'application/octet-stream'
    }
    response = requests.post(url, data=data, headers=headers)
    rescode = response.status_code

    if rescode == 200:
        #print('response.text = ', response.text)
        #print('type=', type(response.text))
        print(response.text)
        hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
        result = hangul.sub('',response.text)
        print(result)

    else:
        print('Error: '+response.text)

    return result