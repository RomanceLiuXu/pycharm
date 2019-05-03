#!/usr/bin/env python
# ­*­ coding: utf­8 

_author_ = 'LiuXu'


# 空函数
def empty():
    pass


# 函数的返回值
def f1():
    name = 'tom'
    age = 20
    sex = 'male'
    return name, age, sex


# print(f1()) # 返回值实际上是一个tuple
# a,b,c= f1()
# print(a,b,c)

# 函数返回值，返回一个函数
def f2(x):
    print(111)
    z = 6

    def f3(y):
        print(x * y + z)  # 内部函数使用了外部函数的参数或局部变量，称为闭包

    return f3


# fn = f2(2)
# fn(10)

# 递归函数: 一个函数在内部调用自身，这个函数就是递归函数

# 计算x的y次方
def calc(x, y):
    if y == 0:
        return 1
    else:
        return x * calc(x, y - 1) # 不停的调用自己，递归太深会出现栈溢出


print(calc(2, 3))
