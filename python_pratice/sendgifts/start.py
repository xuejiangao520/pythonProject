#!/usr/bin/env python3.8

# -*- coding: utf-8 -*-
# @Time : 2020/11/30 21:56
# @Author : xuejiangao
# @FileName: start.py
# @Software: PyCharm
# @E-mail : 
# @Blog :
from send import send
from show import show

"""
1、 from…import 是复制了一份到本地
2、import … 是引用了变量的地址
可以打印id来看地址是否一直
"""

if __name__ == '__main__':
    send()
    show()