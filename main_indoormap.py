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
    continue_dist, realnotice, link_name ,next_name =  link.direction(path,fin)

    link = link.notice(continue_dist, realnotice, link_name, next_name)
    print("link =", link)

    # while fin != strt:
    #     node_info = {"LOTTERIA": "n1", "BEANPOLE": "n2", "LACOSTE": "n3", "STARBUCKS": "n4", "IKEA": "n5", "ZARA": "n6",
    #                  "SUBWAY": "n7", "THOMBROWNE": "n8"}
    #
    #     while ocr1 == [0] and ocr2 == [0]:
    #         ocr1 = total_ocr1()
    #         ocr2 = total_ocr2()
    #         # ocr 로 간판 문구 확인
    #     if ocr1 != [0]:
    #         start = ocr1
    #     elif ocr2 != [0]:
    #         start = ocr2
    #     print('start1 = ', start)
    #
    #     while start not in node_info:
    #         print('not in node list')
    #         while ocr1 == [0] and ocr2 == [0]:
    #             ocr1 = total_ocr1()
    #             ocr2 = total_ocr2()
    #             # ocr 로 간판 문구 확인
    #         ocr1 = total_ocr1()
    #         ocr2 = total_ocr2()
    #         if ocr1 != [0] and ocr1 in node_info:
    #             start = ocr1
    #         elif ocr2 != [0] and ocr2 in node_info:
    #             start = ocr2
    #
    #         print('start2 = ', start)

    # while fin != strt:
    #     node_info = {"LOTTERIA": "n1", "BEANPOLE": "n2", "LACOSTE": "n3", "STARBUCKS": "n4", "IKEA": "n5", "ZARA": "n6",
    #                  "SUBWAY": "n7", "THOMBROWNE": "n8"}
    #
    #     # 오른쪽 캠
    #     ocr1 = total_ocr1()
    #
    #     # 왼쪽 캠
    #     ocr2 = total_ocr2()
    #
    #     start = "none"
    #     # ocr 로 간판 문구 확인
    #     if ocr1 != [0]:
    #         start = ocr1
    #         strt = node_info[start]
    #     elif ocr2 != [0]:
    #         start = ocr2
    #         strt = node_info[start]
    #
    #     print(start)

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