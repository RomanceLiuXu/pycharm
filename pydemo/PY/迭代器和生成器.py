#!/usr/bin/env python
# ­*­ coding: utf­8 

_author_ = 'LiuXu'

""""
迭代器iterator：用来访问集合元素的一种方式,可以记录迭代的位置
"""

nums = [3, 4, 1, 5, 6, 3, 7]
it = iter(nums)  # 用来获取迭代器
print(type(it))

print(next(it))  # 使用next()函数获取迭代器的下一个元素，只能往前不能后退

# 使用for..in循环遍历迭代器
for i in it:
    print(i)

""""
生成器generator:在循环过程中依次计算获取值得对象
创建生成器的方式：
    方式1：把一个列表对象生成式的[]改为()
    方式2：在函数中使用yield关键字，此时函数就变成一个生成器函数
"""
# 方式1：把一个列表对象生成式的[]改为()
generator = (i for i in range(1, 100))

# 获取生成器的下一个元素
print(next(generator))  # 获取时才生成值，类似于oracle中的sequence
print(type(generator))

for i in generator:
    print(i)

print('-' * 90)


# 方式2：在函数中使用yield关键字，此时函数就变成一个生成器函数
def gen():
    print('one')
    yield 3
    print('two')
    yield 7
    print('three')
    yield 35
    print('end')


""""
生成器函数与普通函数的执行流程不一样：
普通函数是顺序执行，执行到最后一行或遇到return时结束
生成器函数是在每次调用next()时执行，遇到yield语句就返回，下一次调用next()时会从上次返回的yield语
句处继续执行
"""
g = gen()  # generator类型
print(type(g))
for i in g:
    print(i)
