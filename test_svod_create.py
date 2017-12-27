#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 17:03
# @Author  : huanghe
# @Site    : 
# @File    : test_svod_create.py
# @Software: PyCharm

import requests
import json
from db_fixture import mongo_db


headers = {
    'Accept' : 'application/json',
    'Connection' : 'keep-alive',
    'Content-Type' : 'application/json'
}
db = mongo_db.DB()
collec = db.getConnection(table_name='aquapaas',connection_name='svod')
for i in collec.find({'type':'create ticket ex asset'}):
    content = i['content']
    print(content)
    #r = requests.post(url,data=json.dumps(content),headers=headers)
    #print(r.text)
#r = requests.post("http://10.50.3.88:8090/aquapaas/sdp/ticket/external",data=json.dumps(payload),headers=headers)
#print(json.dumps(r.text))
