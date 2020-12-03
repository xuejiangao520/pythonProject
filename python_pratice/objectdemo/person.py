#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/1 13:30
# @Author : gaoxuejian
# @Site : 
# @File : person.py
# @Software: PyCharm

"""
class 类名：
   静态属性
   动态方法

属性：姓名、性别、年龄、存款金额。。

方法：吃、睡、跑。。。
"""


class Person:
    name: str = None
    age: int = 0
    gender = "男"
    ##私有属性
    __money: float = 0

    def __init__(self, name, age, gender, money):
        # print("构造函数")
        self.name = name
        self.age = age
        self.gender = gender
        self.__money = money

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    @classmethod  # 类方法
    def run(self):
        print(f"{self.name} is running")

    def money(self):
        print(f"月工资是 {self.__money}")


class FunnyMan(Person):
    skill: str = ""

    def __init__(self, skill, name, age, gender, money):
        self.skill = skill
        # self.name = name
        # self.age = age
        # self.gender = gender
        # self.money = money
        super().__init__(name, age, gender, money)

    def money(self):
        print(f"月工资是 {self.money}")

    def fun(self):
        print(f"{self.name} is funny,his skill is {self.skill}")

    # pass


sm = Person("SM", 20, "男", 20000)
sm.money()
print(sm.money)
st = FunnyMan("单口相声", "ST", 20, "男", 10000)
st.money()
print(st.name)

st.fun()

# p_ls = Person("李四", 20, "男", 1000)
# p_ls
# # 通过实例化对象来调用类属性和方法
# p_zs = Person()
# # p_zs.run()
# print(p_zs.name)
#
# # 通过类调用
#
# print(Person.age)
# # 不可以通过类直接调用方法
# Person.run()
# 通过实例化对象来调用类属性和方法
# p_ls = Person("李四", 20, "男", 1000)
# p_ls = Person()
# print(p_ls.name)
# # p_ls.run()
# p_ls.name = "王五"
# print(p_ls.name)
# Person.name = "default_name"
# print(Person.name)
# print(p_ls.name)

#
# p_zl = Person()
# print(p_zl.name)
