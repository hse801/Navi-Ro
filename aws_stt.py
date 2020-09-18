from __future__ import print_function
import time
import boto3
import pyaudio
import wave
import urllib.request
import json


def main_stt():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output1.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Start to record the audio.")

    frames = []

    for i in range(1, int(RATE / CHUNK * RECORD_SECONDS)):
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

    s3 = boto3.client('s3')
    bucket_name = 'prociegoo'
    s3.upload_file(WAVE_OUTPUT_FILENAME, bucket_name, WAVE_OUTPUT_FILENAME)

    transcribe = boto3.client('transcribe')
    job_name = "hse15"
    #job_uri = "https://S3 endpoint/test-transcribe/answer2.wav"
    #job_uri = "https://s3.ap-northeast-2.amazonaws.com/prociegoo/KoreanTrans.json/TranscribeTest.mp3"
    #job_uri = "C:/Users/Park Jieun/PycharmProjects/project/output1.wav"
    job_uri = "s3://prociegoo/output1.wav"
    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': job_uri},
        MediaFormat='wav',
        LanguageCode='ko-KR',
        MediaSampleRateHertz=44100
    )
    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            transcribe.delete_transcription_job(TranscriptionJobName=job_name)
            break
        print("Not ready yet...")
        time.sleep(30)
    print(status)

    if status['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
        response = urllib.request.urlopen(status['TranscriptionJob']['Transcript']['TranscriptFileUri'])
        data = json.loads(response.read())
        text = data['results']['transcripts'][0]['transcript']
        print(text)

    return text
