#!/usr/bin/env python
# ­*­ coding: utf­8 

_author_ = 'LiuXu'
from collections.abc import Iterable  # 导入模块

""""
迭代：遍历
"""

for i in ['tom', 'jack', 'alice']:
    print(i, end=' ')
print()

for i in ('tom', 'jack', 'alice'):
    print(i, end=' ')
print()

for k, v in {'name': 'alice', 'age': 18, 'sex': 'male'}.items():
    print(k, v)

for i in 'hello':
    print(i)

# 判断对象是否是可以迭代的
print(isinstance('hello', Iterable))

# 获取索引和值
# 方式1：自己获取索引
names = ['tom', 'jack', 'alice']
for i in range(len(names)):
    print(i, names[i])

# 方式2：使用enumerate函数，转换为索引-元素对
print(enumerate(names))
print(isinstance(enumerate(names), Iterable))

print('-' * 90)

# 列表生成式：用来创建list的生成式
# 生成[0,99]的list
nums = list(range(0, 100))
print(nums, type(nums))

print(isinstance(range(1, 10), Iterable))

for i in range(0, 100):
    print(i)

# 生成一个包含[1,100]之间所有3的倍数的list
lst = []
# 方式1：
for i in range(1, 101):
    if i % 3 == 0:
        lst.append(i)
print(lst)
# 方式2:
ls = [i for i in range(1, 101) if i % 3 == 0]
print(ls)
