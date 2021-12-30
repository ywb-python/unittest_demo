#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/25 19:39
# @Author  : ywb
# @Site    : 
# @File    : all.py
# @Software: PyCharm


import unittest
from HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('./testcases', pattern='test_*.py')
    report_file = 'report/test_case_detail.html'
    fp = open(report_file, 'wb')
    runner = HTMLTestRunner(stream=fp,title='unittest的测试报告', description='目前所有报告的结果')
    runner.run(suite)
    fp.close()

