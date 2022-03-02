# !/usr/bin/python
# -*-coding:utf-8 -*-
import requests
import json
import Cookie

coo = Cookie.Coo
time = Cookie.createtime
url = 'http://api.admin-gate.ayibang.cn:8086/v1/customer/refund/listAudit'
params = {
    "createtime": time,
    "order": "createtime desc",
    "auditStatus": "2",
    "limit": "0,10000",
    "refundItemType": "1",
}

cookies = {
    'AYBADMIN': coo}
res = requests.get(url=url, params=params, cookies=cookies)
text = res.text
jsonzdg = json.loads(text)
a = 0;
for item in jsonzdg['datas']:
    a = a + float(item['refund']['refundAmt'])
print('申请退款合计：' + str("%.2f" % a))
