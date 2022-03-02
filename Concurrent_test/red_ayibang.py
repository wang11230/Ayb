# !/usr/bin/python
# -*-coding:utf-8 -*-
import grequests
import time
# 五十次并发请求，需要的时间。
# start = time.time()
# req_list = [grequests.get('http://red.ayibang.com/coupon/exchange') for i in range(50)]
# res_list = grequests.map(req_list)
# print(time.time() - start)
start = time.time()
req_list = [
    grequests.post('http://red.ayibang.com/coupon/getsmscode', data={'tel': '15333512317 '}) for i in range(100)
    # 多次并发请求
    # grequests.post('http://red.ayibang.com/coupon/getsmscode', data={'tel': ' 15333512317 '}),
    # grequests.post('http://red.ayibang.com/coupon/getsmscode', data={'tel': '15333512317 '}),
    # grequests.post('http://red.ayibang.com/coupon/getsmscode', data={'tel': ' 15333512317 '}),
    # grequests.post('http://red.ayibang.com/coupon/getsmscode', data={'tel': '15333512317'}),
    # grequests.post('http://red.ayibang.com/coupon/getsmscode', data={'tel': '15333512317'}),
    # grequests.post('http://red.ayibang.com/coupon/getsmscode', data={'tel': ' 15333512317'}),
    # grequests.post('http://red.ayibang.com/coupon/getsmscode', data={'tel': ' 15333512317'}),
    # grequests.post('http://red.ayibang.com/coupon/getsmscode', data={'tel': '15333512317 '}),
    # grequests.post('http://red.ayibang.com/coupon/getsmscode', data={'tel': ' 15333512317'}),

]
res_list = grequests.map(req_list)
print(time.time() - start)
print(res_list)
# print(res_list[1].text)
# print(res_list[2].text)
# print(res_list[3].text)
# print(res_list[4].text)
# print(res_list[5].text)
# print(res_list[6].text)
# print(res_list[7].text)
# print(res_list[8].text)
# print(res_list[9].text)