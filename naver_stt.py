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
    RECORD_SECONDS = 3
    WAVE_OUTPUT_FILENAME = "output.wav"
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("목적지를 말하세요.")
    print("음성인식을 시작합니다.")

    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK, exception_on_overflow=False)
        frames.append(data)

    print("음성인식이 완료되었습니다.")

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
        hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
        before_result = hangul.sub('', response.text)
        result = before_result.replace(" ", "")
        print(result, "가 목적지로 설정되었습니다.")
    else:
        print('Error: ' + response.text)

    return result