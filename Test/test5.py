# !/usr/bin/python
# -*-coding:utf-8 -*-
from selenium import webdriver


list1 = {'data': {'list': [{'num': '123', 'date': '11-26'}]}}

for i in list1['data']['list']:
    data = i['num']
    print(type(i))