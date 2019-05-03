#!/usr/bin/env python
# ­*­ coding: utf­8 

_author_ = 'LiuXu'


class Student:
    # pass
    # 类属性:直接在类中定义的属性
    hobby = '吃饭'

    # 类方法:使用@classmethod修饰的方法
    # cls表示当前类
    @classmethod
    def show(cls, msg):
        print(msg, cls.hobby)

    # 静态方法：使用@staticmetho修饰的方法
    @staticmethod
    def show2(msg):
        print(Student.hobby,msg)

    # 实例方法:将self作为第一个参数的方法
    # self表示的是当前类的实例
    def say_hi(self):
        print('Hi，' + self.name)

    def say_hello(self, username='无名氏'):
        print('Hello,' + username)


# 创建类的对象
stu1 = Student()  # 创建Student类的一个实例
stu2 = Student()  # 创建Student类的一个实例

print(stu1, type(stu1))
print(stu2, type(stu2))

# 为对象绑定属性
stu1.name = 'tom'  # 实例属性，通过实例对象添加的属性
stu1.age = 23
stu2.name = 'jack'
stu2.sex = 'male'

print(stu1.name)

# 访问实例方法
stu1.say_hi()  # 调用方法时无需传递self，由解析器调用对象时将当前对象作为self自动传入

stu1.say_hello('kk')

# 访问类属性
print(Student.hobby)
stu1.hobby = '睡觉'  # 为stu1添加了一个实例属性，并不会改变类属性hobby的值，如果当前实例没有则向上找属性
print(stu1.hobby)

# 访问类方法
Student.show('msg')
stu1.show('msg')

Student.show2('ss')