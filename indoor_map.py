import cv2
import matplotlib.pyplot as plt
import numpy as np
# matplotlib.image 를 사용하기 위해선 matplotlib 뿐만 아니라 pillow도 깔아야 한다
import matplotlib.image as mpimg

ppix =[[0 for col in range(245)] for row in range(240)]

# 색상 범위 설정
lower_orange = (100, 200, 200)
lower_orange1 = [100, 200, 200]

upper_orange = (140, 255, 255)
upper_orange1 = [140, 255, 255]

lower_green = (30, 80, 80)
upper_green = (70, 255, 255)

lower_blue = (0, 180, 55)
upper_blue = (20, 255, 200)

color_125 = (0, 255, 255)


# 이미지 파일을 읽어온다
img = mpimg.imread("test2.jpg", cv2.IMREAD_COLOR)

# BGR to HSV 변환
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
width, height = img_hsv.shape[:2]

# 색상 범위를 제한하여 mask 생성

img_mask = cv2.inRange(img_hsv, lower_orange, upper_orange)
# for i in range(240):
#     for j in range(245):
#         if lower_orange <=img_hsv[i][j] <upper_orange :
#             ppix[i][j]=1

# for i in range(width):
#     for j in range(height):
#         if img_hsv[i][j][0] > lower_orange1[0] and img_hsv[i][j][1] > lower_orange1[1] and img_hsv[i][j][2] > lower_orange1[2] and img_hsv[i][j][0] < upper_orange1[0] and img_hsv[i][j][1] < upper_orange1[1] and img_hsv[i, j, 2] < upper_orange1[2]:
#             ppix[i][j] = 1
#             print('i(width) = ', i)
#             print('j(height) = ', j)
for i in range(width):
    for j in range(height):
        if sv[i][j][0] < upper_orange1[0] and img_hsv[i][j][1] < upper_orange1[1] and img_hsv[i, j, 2] < upper_orange1[2]:
            ppix[i][j] = 1
            print('i(width) = ', i)
            print('j(height) = ', j)

print(ppix)

img_result = cv2.bitwise_and(img, img, mask=img_mask)

# 결과 이미지 생성

imgplot = plt.imshow(img_result)
plt.show()

