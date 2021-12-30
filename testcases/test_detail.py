#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/25 19:37
# @Author  : ywb
# @Site    : 
# @File    : test_detail.py
# @Software: PyCharm
from common.my_utils import MyUnit


class TestDetail(MyUnit):

    def test_good_detail(self):
        print('测试商品详情')

    def test_coupon_detail(self):
        print('测试优惠券详情')

    def test_shopcart_detail(self):
        print('测试购物车详情')