import boto3
import cv2
import time
import numpy as np
import json
import threading

ocr_result1 = [0]
ocr_result2 = [0]


def total_ocr1():
    # ocr_result1=""

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    bucket_name = "prociegoo"
    aws_region = "ap-northeast-2"
    filename = "testimggg1.jpg"

    # S3 Upload Function

    def uploadImage():
        # Create an S3 client
        s3 = boto3.client('s3')
        # Uploads the given file using a managed uploader, which will split up large
        # files automatically and upload parts in parallel.
        s3.upload_file(filename, bucket_name, filename)
        print('Image uploaded to S3 Bucket.')

    # Rekognition Detect Text Function
    def detectText():
        #ocr_result1 = [0]
        global ocr_result1

        rekognitionClient = boto3.client('rekognition', aws_region)
        response = rekognitionClient.detect_text(
          Image = {
             'S3Object': {
                'Bucket': bucket_name,
                'Name': filename,
                #'Bytes': filename.tobytes()
             }
          }
        )

        print('The image contains the following text:'  )
        # Parse the JSON response from Amazon Rekognition, and print out detecd lines of text.
        for text in response['TextDetections']:
                if text['Type'] == 'LINE':
                   print ('Text: ' + text['DetectedText'] + ' was detected on line ' + str(text['Id']) + ' with confidence of ' + str(text['Confidence']))
                ocr_result1=text['DetectedText']

    # Campture Image Fution
    def captureImage():

        #cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        ret, filename = cap.read()
        cv2.imwrite("testimggg1.jpg", filename)
        cv2.waitKey(0)

    # while True 없애면 1번만 돌아가게 할 수 있음, while True 넣은 상태에서 사진 바꾸면 바꾼대로 잘 출력됨, 텀 시간 조절 가능한듯
    def main():
        # global ocr_result1
        print('Started...')
        #while True:
        captureImage()
            # wait for thbe camptured
        uploadImage()
            # waior the image to uploaded
        detectText()
    main()
    print("ocr_result1", ocr_result1)
    return ocr_result1


#############################################
def total_ocr2():

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    bucket_name = "prociegoo"
    aws_region = "ap-northeast-2"

    filename = "testimggg2.jpg"


    # S3 Upload Function
    def uploadImage():

        #Create an S3 client
        s3 = boto3.client('s3')
        # Uploads the given file using a managed uploader, which will split up large
        # files automatically and upload parts in parallel.
        s3.upload_file(filename, bucket_name, filename)
        print('Image uploaded to S3 Bucket.')

    # Rekognition Detect Text Function
    def detectText():
        global ocr_result2
        rekognitionClient = boto3.client('rekognition', aws_region)
        response = rekognitionClient.detect_text(
          Image={
             'S3Object': {
                'Bucket': bucket_name,
                'Name': filename,
                #'Bytes': filename.tobytes()
             }
          }
        )

        print('The image contains the following text:'  )
        # Parse the JSON response from Amazon Rekognition, and print out detecd lines of text.
        for text in response['TextDetections']:
            if text['Type'] == 'LINE':
               print ('Text: ' + text['DetectedText'] + ' was detected on line ' + str(text['Id']) + ' with confidence of ' + str(text['Confidence']))
            #             if text['DetectedText']=="":
            #                 print("no")
            ocr_result2=text['DetectedText']

    # Campture Image Fution
    def captureImage():
        # cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        ret, filename = cap.read()
        cv2.imwrite("testimggg2.jpg", filename)
        cv2.waitKey(0)

    # while Ture 없애면 1번만 돌아가게 할 수 있음, while True 넣은 상태에서 사진 바꾸면 바꾼대로 잘 출력됨, 텀 시간 조절 가능한듯
    def main():
        print('Started...')
        #while True:
        captureImage()
            # wait for thbe camptured
        uploadImage()
            # waior the image to uploaded
        detectText()

    main()
    print("ocr_result2", ocr_result2)
    return ocr_result2
