from multiprocessing import Process

from yolo_lidar import final, startyolo
from main_indoormap import main


def repeat():
    con = 0
    while con == 0:
        startyolo()
        con = main()


p1 = Process(target=final)
p2 = Process(target=main)

if __name__ == '__main__':
    p2.start()
    p1.start()