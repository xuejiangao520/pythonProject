#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/2 14:14
# @Author : gaoxuejian
# @Site : 
# @File : test_os1.py
# @Software: PyCharm

import os

# os.mkdir("testdir")
# print(os.listdir("./"))

# os.removedirs("testdir")
# print(os.getcwd())
# print(os.name)

# os.removedirs("o")
print(os.path.exists("b"))
if not os.path.exists("b"):
    os.mkdir("b")
if not os.path.exists("b/test.txt"):
    f = open("b/test.txt", "w")
    f.write("hello,os using")
    print(f)
