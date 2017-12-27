#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/27 13:55
# @Author  : huanghe
# @Site    : 
# @File    : test_create.py
# @Software: PyCharm
import unittest
import requests
import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import mongo_db
import json

class CreateTest(unittest.TestCase):


    def setUp(self):
        headers = {
            'Accept': 'application/json',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json'
        }
        self.base_url = 'http://10.50.3.88:8090/aquapaas/sdp/ticket/external'
        self.header = headers
        db = mongo_db.DB()
        self.collection = db.getConnection(table_name='aquapaas',connection_name='svod')

    def tearDown(self):
        print(self.result)

    def test_create_ticket_ex_asset(self):
        content = self.collection.find({'type':'create ticket ex asset'})
        for i in content:
            content = i['content']
            print(content)
        r = requests.post(url=self.base_url, data=json.dumps(content), headers=self.header)
        self.result = r.json()
        self.assertIn(self.result['status'],{200,409})
        #self.assertEqual(self.result['status'],200)

    if __name__ == '__main':
        unittest.main()