#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/27 14:44
# @Author  : huanghe
# @Site    : 
# @File    : run_tests.py
# @Software: PyCharm
import time,sys
sys.path.append('./interface')
sys.path.append('./db_fixture')
from HTMLTestRunner import HTMLTestRunner
import unittest

test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Aquapaas Interface Test Report',
                            description='Implementation Example with: ')
    runner.run(discover)
    fp.close()