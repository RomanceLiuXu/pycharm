#!/usr/bin/env python
# ­*­ coding: utf­8 

_author_ = 'LiuXu'

""""
匿名函数：没有名字的函数，使用lambda关键字
"""

nums = [2, 5, 6, 7, 8, 12, 4]
# 对集合中的元素进行*2+1操作
nums_new = list(map(lambda x: x * 2 + 1, nums))
print(nums_new)

# 将匿名函数赋值给变量(不建议)
a = lambda x: x + 1
print(a(2))

print('-' * 90)

""""
装饰器：在代码运行期间动态增加功能，称为装饰器decoration，类似于AOP
"""


# 定义一个装饰器，为函数添加打印日志的功能
def log(fn):
    def wrapper(*args, **kwargs):
        print('开始执行%s()函数' % fn.__name__)
        fn(*args, **kwargs)
        print('执行%s()函数结束' % fn.__name__)

    return wrapper  # 返回装饰函数


# 应用装饰器
@log
def even(lst):
    for i in lst:
        print(i)


even(nums)
