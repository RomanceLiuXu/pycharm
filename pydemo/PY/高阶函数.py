#!/usr/bin/env python
# ­*­ coding: utf­8 

_author_ = 'LiuXu'

""""
高阶函数：一个函数接收另一个函数作为参数，这种函数称为高阶函数
"""

nums = [-12, -3, 4, 2, -4]


# 定义一个函数，用来检查数字是否大于5
def f1(x):
    if x > 5:
        return True
    else:
        return False


# 定义高阶函数，用来过滤列表中的元素
def fn(fun, lst):
    """
    将列表中符合条件的元素筛选出来，返回一个新列表
    :param fun:
    :param lst:
    :return:
    """
    new_list = []
    for i in lst:
        if fun(i):
            new_list.append(i)
    return new_list


# 调用高阶函数
nums1 = fn(f1, nums)
print(nums1)

# 内置高阶函数，filter(),用于过滤序列
nums2 = filter(f1, nums)  # 返回的为filter对象
print(list(nums2))


# 内置高阶函数map(),用于处理序列
def f3(x):
    return x + 1;


# 给每个元素进行加1操作
nums3 = map(f3, nums)
print(list(nums3))

# 内置高阶函数,sort(),用于排序
print(sorted(nums))
print(sorted(nums,key=abs))
