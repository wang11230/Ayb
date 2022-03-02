# !/usr/bin/python
# -*-coding:utf-8 -*-
import time
from datetime import datetime
import  pytz
from time import sleep

i = 0
while i <= 10:
    tz = pytz.timezone('Asia/Shanghai')
    t = datetime.fromtimestamp(int(time.time()),
    tz).strftime('%Y-%m-%d %H:%M:%S.%f')
    print(type(t))
    i += 1
    sleep(0.2)
