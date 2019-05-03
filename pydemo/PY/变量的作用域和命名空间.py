#!/usr/bin/env python
# ­*­ coding: utf­8 

_author_ = 'LiuXu'

"""
变量作用域scope：指的是变量生效的区域
两种作用域：
1.全局作用域
函数以外的区域都是全局作用域
在全局作用域中定义的变量，都是全局变量
2.函数作用域，也称为局部作用域
函数内的区域，每调用一次函数就会创建一个新的函数作用域
在函数作用域中定义的变量，都是局部变量
变量的查找顺序：
先在当前作用域中查找，如果没有则向上一级作用域中查找，直到查找全局作用域，如果还是没有，则报错
"""

a = 5  # 全局变量

if True:
    c = 2  # 全局变量，在python中没有块级作用域


def fn():
    b = 2
    print('函数内部，a=', a)
    print('函数内部，b=', b)
    print('函数内部，c=', c)


def f1():
    x = 2

    def f2():
        x = 3
        print(x)


print('-' * 90)


def fn2():
    # a = 10 # 在函数中为变量赋值时，默认都是为局部变量赋值
    # 如果你希望在函数中去修改全局变量，要是用global关键字
    global a
    a = 10
    print('函数内部，a=', a)


fn2()
print('函数外部，a=', a)

"""
命名空间namespace:指的是变量存储的位置，每一个变量都要存储在指定的命名空间中

每个作用域都有一个对应的命名空间
全局命名空间；函数命名空间
命名空间实际上就是一个字典，是一个专门用来存储变量的字典
"""

# locals() 获取当前作用域的命名空间
scope = locals()
print(scope, type(scope))

# 通过scope操作命名空间中的变量
print(scope['a'])
scope['c'] = 'tom'
scope['a'] = 666
scope['z'] = 'alice'
print(scope['c'])
print(scope['z'])
print(scope['a'])

def fn3():
    a = 888
    scope = locals()# 在函数中调用locals(),获取到的是函数的命名空间
    scope['b'] = 222
    print(scope)
    print(scope['b'])

# globals() 可以在任意位置获取全局命名空间
    global_scope = globals()
    print(global_scope)

fn3()