a = 1


def fun():
    global a
    a = 2
    print(id(a))
    print(f"变量a的值：{a}")
    """
    1.函数里可以调用外部变量 ，
    2.不可以改变外部变量，
    3.如果改变可以设置成为全局变量 global，
    4.通过id（）方法可以打印id的内存地址
    5.方法默认返回是None
    """
    print("这是一个方法")
    # return True


# print(a)
# fun()
# print(a)
# print(id(a))
# print(fun())
if __name__ == '__main__':
    print("start")
    fun()
    print("end")
