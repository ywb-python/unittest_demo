#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/30 10:59
# @Author  : ywb
# @Site    : 
# @File    : test_ddt.py
# @Software: PyCharm


import unittest
from ddt import ddt, data, unpack


@ddt
class TestDdt(unittest.TestCase):

    @data("UI自动化测试")
    def test_01_case(self, args):
        print(args)

    @data("功能测试", "自动化测试")
    def test_02_case(self, args):
        print(args)

    @data(("电商", "游戏"))
    def test_03_case(self, args):
        print(args)

    @data(("西游记", "吴承恩"), ("三国演义", "罗贯中"))
    def test_04_case(self, args):
        print(args)

    @data(("西游记", "吴承恩"), ("三国演义", "罗贯中"))
    @unpack
    def test_05_case(self, book, author):
        print(f'{book}的作者是{author}')

    @data(["水浒传", "施耐庵"], ["红楼梦", "曹雪芹"])
    @unpack
    def test_06_case(self, book, author):
        print(f'{author}写了{book}')

    @data({"name": "史记", 'author': "司马迁"}, {"name": "三国志", "author": "陈寿"})
    @unpack
    def test_07_case(self, name, author):
        print(f'{author}写了{name}')


if __name__ == '__main__':
    unittest.main()
