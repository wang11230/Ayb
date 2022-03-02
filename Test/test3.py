# !/usr/bin/python
# -*-coding:utf-8 -*-
import requests
import time
import json
import Cookie

coo = Cookie.Coo
time = Cookie.createtime
url = 'http://api.admin-gate.ayibang.cn:8086/v1/paytrade/trade/lists'
params = {
    "createChannel": "1",
    "createtime": time,
    "limit": '0,3000',
    "order": "id desc",
    "result": "1",
    "tradeChannel": "{20,30}",  # 付款方式
    "tradeType": "",  # 账务类型
}

cookies = {
    'AYBADMIN': coo}
res = requests.get(url=url, params=params, cookies=cookies)
text = res.text
jsoncz = json.loads(text)
payAmount = 0;
refundAmt = 0;
for item in jsoncz['datas']:
    payAmount = payAmount + float(item['payment']['payAmount'])
    refundAmt = refundAmt + float(item['payment']['refundAmt'])

pay = payAmount + refundAmt
print("时间范围等于" + time + "时：")
print('收款：' + str("%.2f" % payAmount) + '\n' + '退款：' + str("%.2f" % refundAmt) + '\n' + '实际收入：' + str("%.2f" % pay))
