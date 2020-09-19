import requests

client_id = '9sf3slvfnj'
client_secret = '8Nduivr0ilu6UrqgfbI5kvvchPQWxqU1iTHZo2oI'

lang = 'Kor'
url = 'https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=' + lang

data = open('stt_test.m4a', 'rb')

headers = {
    'X-NCP-APIGW-API-KEY-ID': client_id,
    'X-NCP-APIGW-API-KEY': client_secret,
    'Content-Type': 'application/octet-stream'
}
response = requests.post(url, data=data, headers=headers)
rescode = response.status_code

if rescode == 200:
    print(response.text)
else:
    print('Error: '+response.text)