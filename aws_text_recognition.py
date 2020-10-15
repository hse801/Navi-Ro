import boto3
import cv2


def total_ocr1():
    ocr_result1 = [0]
    cap = cv2.VideoCapture(0)
    bucket_name = "prociegoo"
    aws_region = "ap-northeast-2"
    filename = "testimggg1.jpg"

    def uploadImage():
        s3 = boto3.client('s3')
        s3.upload_file(filename, bucket_name, filename)

    def detectText():
        rekognitionClient = boto3.client('rekognition', aws_region)
        response = rekognitionClient.detect_text(

            Image={
                'S3Object': {
                    'Bucket': bucket_name,
                    'Name': filename,
                }
            }
        )

        for text in response['TextDetections']:
            if text['Type'] == 'LINE':
                ocr_result1.append(text['DetectedText'])

    def captureImage():
        ret, filename = cap.read()
        cv2.imwrite("testimggg1.jpg", filename)
        cap.release()

    def main():
        captureImage()
        uploadImage()
        detectText()
    main()

    return ocr_result1


def total_ocr2():
    ocr_result2 = [0]
    cap = cv2.VideoCapture(2)
    bucket_name = "prociegoo"
    aws_region = "ap-northeast-2"
    filename = "testimggg2.jpg"

    def uploadImage():
        s3 = boto3.client('s3')
        s3.upload_file(filename, bucket_name, filename)

    def detectText():
        rekognitionClient = boto3.client('rekognition', aws_region)
        response = rekognitionClient.detect_text(

            Image={
                'S3Object': {
                    'Bucket': bucket_name,
                    'Name': filename,
                }
            }
        )

        for text in response['TextDetections']:
            if text['Type'] == 'LINE':
                ocr_result2.append(text['DetectedText'])

    def captureImage():
        ret, filename = cap.read()
        cv2.imwrite("testimggg2.jpg", filename)
        cap.release()

    def main():
        captureImage()
        uploadImage()
        detectText()
    main()

    return ocr_result2