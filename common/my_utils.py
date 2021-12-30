#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/26 20:51
# @Author  : ywb
# @Site    : 
# @File    : my_utils.py
# @Software: PyCharm


import unittest


class MyUnit(unittest.TestCase):
    def setUp(self) -> None:
        print('用例执行前的准备')

    def tearDown(self) -> None:
        print('用例结束后的清理工作')

    @classmethod
    def setUpClass(cls) -> None:
        print('测试类之前的准备')

    @classmethod
    def tearDownClass(cls) -> None:
        print('测试类结束后的清理工作')
