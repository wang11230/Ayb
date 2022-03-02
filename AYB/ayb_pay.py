# !/usr/bin/python
# -*-coding:utf-8 -*-
import requests
import time
import json
import Cookie

coo = Cookie.Coo
createtime = Cookie.createtime
limit = '0,100'
url = 'http://api.admin-gate.ayibang.cn:8086/v1/paytrade/trade/lists'
params = {
    "createChannel": "1",
    "createtime": createtime,
    "limit": limit,
    "order": "id desc",
    "result": "1",
    "tradeChannel": "{20,30}",  # 付款方式
    "tradeType": "",  # 账务类型
}

cookies = {
    'AYBADMIN': coo}

cont = 0;
size = 1;
payAmount = 0;
refundAmt = 0;
while (size > 0):
    res = requests.get(url=url, params=params, cookies=cookies)
    text = res.text
    jsoncz = json.loads(text)
    size = len(jsoncz['datas'])
    cont = cont + size
    for item in jsoncz['datas']:
        payAmount = payAmount + float(item['payment']['payAmount'])
        refundAmt = refundAmt + float(item['payment']['refundAmt'])
    limit = str(cont) + ',100'
    print('正在计算中...' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    params = {
        "createChannel": "1",
        "createtime": createtime,
        "limit": limit,
        "order": "id desc",
        "result": "1",
        "tradeChannel": "{20,30}",  # 付款方式
        "tradeType": "",  # 账务类型
    }

pay = payAmount + refundAmt
print("时间范围等于" + createtime + "时：")
print('收款：' + str("%.2f" % payAmount) + '\n' + '退款：' + str("%.2f" % refundAmt) + '\n' + '实际收入：' + str("%.2f" % pay))
