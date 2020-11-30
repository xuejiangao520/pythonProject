#!/usr/bin/env python3.8

# -*- coding: utf-8 -*-
# @Time : 2020/11/30 21:41
# @Author : xuejiangao
# @FileName: sendgift.py
# @Software: PyCharm
# @E-mail : 
# @Blog :

have_gift =False

#发礼物方法
def send():
    print("发礼物啦！")
    global have_gift
    have_gift = True

#展示礼物

def show():
    if have_gift == True:
        print("收到礼物啦！开心")
    else:
        print("没有礼物！")

if __name__ == '__main__':
    send()
    show()