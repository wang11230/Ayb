# !/usr/bin/python
# -*-coding:utf-8 -*-
import requests
import json
import Cookie

coo = Cookie.Coo
time = Cookie.createtime
url = 'http://api.admin-gate.ayibang.cn:8086/v1/ordercombo/corder/lists'
params = {
    "createtime": time,
    "order": "createtime desc",
    "status": "20",
    "limit": "0,10000",
}

cookies = {
    'AYBADMIN': coo}
res = requests.get(url=url, params=params, cookies=cookies)
text = res.text

jsoncz = json.loads(text)

a = 0;
for item in jsoncz['datas']:
    a = a + float(item['pay']['discountExpense'])
print('慧家集套餐购买合计：' + str(a))
