# !/usr/bin/python
# -*-coding:utf-8 -*-
import requests
import json
import Cookie

coo = Cookie.Coo
time = Cookie.createtime
url = 'http://api.admin-gate.ayibang.cn:8086/v1/contract/receipt/lists'
params = {
    "confirmTime": time,
    "createtime": "",
    "order": "applyTime desc",
    "status": "3",
    "tradeType": "1",
    "payMethod": "{2,3}",
    "limit": "0,10000",
}

cookies = {
    'AYBADMIN': coo}
res = requests.get(url=url, params=params, cookies=cookies)
text = res.text

jsonzdg = json.loads(text)
a = 0;
for item in jsonzdg['datas']:
    a = a + float(item['receipt']['payMoney'])
b = a / 100
print(time)
print('签约订单收款合计：' + str(b))
