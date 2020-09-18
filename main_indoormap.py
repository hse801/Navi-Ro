from __future__ import print_function
from aws_stt import main_stt
from aws_text_recognition import total_ocr1
from aws_text_recognition import total_ocr2
from set_map import *
import boto3
import time
import cv2
import numpy as np
import json

import pyaudio
import wave
import urllib.request


def main():
    from set_map import bring, link

    path,strt,fin = bring.main()

    #link = link.direction(path)
    continue_dist, realnotice, link_name, next_name = link.direction(path, fin)

    link = link.notice(continue_dist, realnotice, link_name, next_name)
    print("link =", link)


main()

#info에 보내줄 path_node 함수;
# def send_node():
#     return path_node


#t1 = Thread(target = main, args =(""))
#t2 = Thread(target = yolo_lidar, args =(""))
#t3 = Thread(target = test, args =(""))

#t1.start()
#t2.start()
#t3.start()