from __future__ import print_function
from aws_stt import main_stt
from aws_text_recognition import total_ocr1
from aws_text_recognition import total_ocr2
import boto3
import time
import cv2
import numpy as np
import json

import pyaudio
import wave
import urllib.request


def main():

    from set_map import set_node, link, navi
    # 오른쪽 캠
    ocr1 = total_ocr1()

    # 왼쪽 캠
    ocr2 = total_ocr2()

    text_result = main_stt()
    #text_result = "자라."

    if text_result == "빈폴.":
        stt_result = "BEANPOLE"
    elif text_result == "라코스테.":
        stt_result = "LACOSTE"
    elif text_result == "스타벅스.":
        stt_result = "STARBUCKS"
    elif text_result == '서브웨이.':
        stt_result = 'SUBWAY'
    elif text_result == '이니스프리.':
        stt_result = 'innisfree'
    elif text_result == '톰 브라운':
        stt_result = 'THOMBROWNE'
    elif text_result == '자라.':
        stt_result = 'ZARA'
    # elif text_result == '톰브라운.':
    #     stt_result = ''

    #print(stt_result)

    # ocr 로 간판 문구 확인
    if ocr1 == [0]:
        start = ocr2
    elif ocr2 == [0]:
        start = ocr1

    # 시작 지점의 노드 확인
    strt_node = set_node.name(start)

    print(strt_node)

    #목적지 입력 받기
    fin = stt_result

    fin_node = set_node.name(fin)
    print(fin_node)

    #경로 찾기
    path = navi.path(strt_node, fin_node)

    print("path =", path)


    #경로 검출

    #노드 간 거리 구하기

    # strt_locat = link.locat(strt_node)
    # fin_locat = link.locat(fin_node)
    #
    # print("strt_locat =",strt_locat)
    # print("fin_locat =", fin_locat)

    #경로에 따라 총 거리 구하기
    dist, path_node = link.dist(path)
    print("dist =", dist)
    print("path_node =", path_node)

    link = link.direction(path_node)

    print("link =", link)


main()
