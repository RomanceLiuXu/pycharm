#!/usr/bin/env python
# ­*­ coding: utf­8 

_author_ = 'LiuXu'


# 函数
# help(print())

# 自定义函数
def calc(num1, num2):
    return num1 + num2


# print(calc(1,2))

# 参数类型检查
def my_abs(x):
    """
    计算绝对值
    :param x: 参数
    :return: 返回值
    """
    if not isinstance(x, (int, float)):
        raise TypeError('参数类型不正确')

    if x > 0:
        return x
    else:
        return -x


# print(my_abs(-1))
# 默认参数，即有默认值的参数
def my_pow(x, y=2):
    if y == 0:
        return 1;
    res = x
    for i in range(y - 1):
        res *= x
    return res


# print(my_pow(2,3))
# print(my_pow(3))

# 可变参数，使用*号，表示参数个数是可变的
# 不建议将可变参数放在最前面
def my_sum(x, *y):
    print(x)
    print(y)  # 接受到的实际是一个元组tuple


def my_sum2(*x, y):
    print(x)
    print(y)  # 接受到的实际是一个元组tuple


# my_sum(1,2,3,4)
# my_sum2(1,2,3,y=4) # 需要自己指定参数名
# 对于可变参数，可以直接传入list或是tuple，只需要将必选参数前加一个*
# nums = [2,3,4,5,6,7,7]
# my_sum(4,*nums)

# 关键字参数，使用**，也表示参数个数是可变的，但传递的参数是带名称的参数
def f1(x, **y):
    print(x)
    print(y)  # 实际接受的是一个dict


# f1(1,a=3,b=4,c=5)

user = {'id': 188, 'name': 'tom', 'age': 18}
f1(4, **user)


# 命名关键字参数，限制关键字的名字，使用*分隔，*号后面的参数表示命名关键字参数
def f2(x, *, name, age):
    print(x)
    print(name)
    print(age)


f2(4, name='liuxu', age=12)


# 任意参数

def f3(*args, **reargs):
    print(args)
    print(reargs)


f3(1, 3, 4, 5, 'ss', name='aa')
