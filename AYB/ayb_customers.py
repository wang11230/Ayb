# !/usr/bin/python
# coding=utf-8
import requests
import json
import Cookie

coo = Cookie.Coo
time = Cookie.createtime
url = 'http://api.admin-gate.ayibang.cn:8086/v1/customer/recharge/lists'
params = {
    "bTime": "2021-11-01T00:00:00.000Z",
    "eTime": "2021-11-08T00:00:00.000Z",
    "createtime": time,
    "order": "createtime desc",
    #    "custUuid": "2213613",
    "status": "2",
    "limit": "0,10000",
}
cookies = {
    'AYBADMIN': coo}
res = requests.get(url=url, params=params, cookies=cookies)
text = res.text
jsonhy = json.loads(text)
a = 0;
for item in jsonhy['datas']:
    a = a + float(item['recharge']['amt'])
print('会员充值合计：' + str(a))

