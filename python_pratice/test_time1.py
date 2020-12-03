#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/2 14:33
# @Author : gaoxuejian
# @Site : 
# @File : test_time1.py
# @Software: PyCharm

"""
time.asctime()  国外的时间格式
time.time()     时间戳
time.sleep(10)  等待
time.localtime()时间戳转成时间元组
time.strftime() 将当前的时间戳转成带个是的时间
例如：time.strftiem("%Y-%m-%d-%H-%M-%S"，time.localtime())

"""
import time

# print(time.asctime())
# print(time.time())
#
# print(time.sleep(10))
#
# print(time.localtime())
# print(time.strftime("%Y年%m.%d.%H.%M.%S", time.localtime()))
#
# print("睡觉了么")


# 获取两天前的时间
now_timetamp = time.time()
before_now = now_timetamp - 60 * 60 * 24 * 2
str_tuple = time.localtime(before_now)
print(print(time.strftime("%Y年%m.%d.%H.%M.%S", str_tuple)))
