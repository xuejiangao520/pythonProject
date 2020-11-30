#!/usr/bin/env python3.8

# -*- coding: utf-8 -*-
# @Time : 2020/11/30 22:03
# @Author : xuejiangao
# @FileName: demo.py
# @Software: PyCharm
# @E-mail : 
# @Blog :


a = 1

def fun():
    global a
    a = 2
    print(f"我是a的变量：{a}")
    print("我是内部函数")
    print(a)
    print(id(a))
    return True

# print(a)
# print(id(a))
"""
1、python 允许在模块里定义 变量和方法的
2、函数里是可以调用外部的变量
3、函数里不允许改变外部变量
4、把外部变量设置为global 全局的，就可以改变它
5、通过 id() 方法可以打印对象的内存地址
6、方法默认返回值 是None
"""

if __name__ == '__main__':

    fun()