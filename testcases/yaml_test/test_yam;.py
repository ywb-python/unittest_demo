#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/30 13:54
# @Author  : ywb
# @Site    : 
# @File    : test_yam;.py
# @Software: PyCharm

import unittest
from ddt import ddt, file_data

@ddt
class TestYaml(unittest.TestCase):

    @file_data('./test_01.yaml')
    def test_01_yaml(self, **kwargs):
        print(kwargs)
