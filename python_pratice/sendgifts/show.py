#!/usr/bin/env python3.8

# -*- coding: utf-8 -*-
# @Time : 2020/11/30 21:56
# @Author : xuejiangao
# @FileName: show.py
# @Software: PyCharm
# @E-mail : 
# @Blog :

# from gift import have_gift
import gift

def show():
    if gift.have_gift == True:
        print("收到礼物啦！开心")
    else:
        print("没有礼物！")
