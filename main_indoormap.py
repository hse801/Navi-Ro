from __future__ import print_function
from threading import Thread
import boto3
import time
import cv2
import numpy as np
import json

import pyaudio
import wave
import urllib.request

from naver_stt import main_stt
from aws_text_recognition import total_ocr1
from aws_text_recognition import total_ocr2
#from lidar_RRRE import yolo_lidar


def main():
    from set_map import bring, link

    path, strt, fin_node, fin = bring.main()

    #link = link.direction(path)
    continue_dist, realnotice, user, next_name, fin = link.direction(path, fin_node, fin)

    link.notice(continue_dist, realnotice, user, next_name,fin)
    #print("link =", link)