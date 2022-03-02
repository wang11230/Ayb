# !/usr/bin/python
# -*-coding:utf-8 -*-
import datetime
from time import sleep

a = 3
b = 4


def buy(buytime):
    while True:
        t = str(datetime.datetime.now())
        if t < buytime:
            print(t + '--时间对比中。')
        else:
            print('ting')
            print('停止计时。')
            break
        sleep(0.5)


print('666')

if __name__ == "__main__":
    buy('2020-11-13 16:22:00.392000')
