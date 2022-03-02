# !/usr/bin/python
# -*-coding:utf-8 -*-
import requests, json

url = 'http://api.admin-gate.demo.ayibang.cn/v1/hero/baserecord/lists'
params = {
    "heroType": "1",
    "leavelineStatus": "2",
    "limit": "0,20",
    "order": "createtime desc",
    "status": "3",
    "svcCity": "taiyuan",
}
cookies = {
    'AYBADMINdemo': 'AWZQMAA1AjMEYQdgWmQGZwcxAz9SNQVvUTcKOFlgVm0HZgVlV2cOO1MxVmkOZVBjUGJQMgZnA28EMFoyUzdWMQ%253D%253D'
}
res = requests.get(url=url, params=params, cookies=cookies)
rest = res.text
jsontest = json.loads(rest)
for item in jsontest['datas']:
    name = item['heroBase']['name']
    heroUuid = item['recordAudit']['heroUuid']
    print(name+","+heroUuid)

