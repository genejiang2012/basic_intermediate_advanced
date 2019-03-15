#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: brother_ma_001_oop_example.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: excersie the oop for python
"""


class MyKlass(object):
    """A example class"""
    x = 'abc'   # 类的属性

    def __init__(self):
        print('self in init={}'.format(id(self)))

    def foo(self):  # 类的方法也是类的属性
        return "My Class"


# print(MyKlass.x)
# print(MyKlass.foo)
# print(MyKlass.__doc__)

a = MyKlass()
print('a={}'.format(id(a)))

print("~"*10)


class MyClass(object):
    """Docstring for MyClass. """

    def __init__(self):
        """TODO: to be defined1. """
        self.x = 123
        print('init')

    def foo(self):
        print('{}'.format(self.x))
        return self.x


class Person(object):
    """Person class"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_age(self):
        print("{} is {}".format(self.name, self.age))


print(MyClass)
print(MyClass())
a = MyClass()
print(a.x)
print(a.foo())

tom = Person('Tom', 28)
jerry = Person('Jerry', 20)
print(tom.name, jerry.age)
jerry.age += 1
print(jerry.age)
jerry.show_age()


class PersonExample(object):
    """docstring for PersonExample"""
    age = 3

    def __init__(self, name):
        self.name = name


print('--------------class------------------')
print(PersonExample.__class__)
print(sorted(PersonExample.__dict__.items()), end='\n\n')

tom_new = PersonExample('Tom')
print('---------------instance tom----------')
print(tom_new.__class__)
print(sorted(tom_new.__dict__.items()), end='\n\n')
print("----------tom's class-----------------")
print(tom_new.__class__.__name__)
print(sorted(tom_new.__class__.__dict__.items()), end='\n\n')


class PersonNew(object):
    """docstring for PersonNew"""
    age = 3
    height = 170

    def __init__(self, name, age=18):
        self.name = name
        self.age = age


tom_2 = PersonNew('Tom')
jerry_2 = PersonNew('Jerry', 20)

PersonNew.age = 30
print(PersonNew.age, tom_2.age, jerry_2.age)

tom_2.name ='TOM father'
print(tom_2.name)


print(PersonNew.height, tom_2.height, jerry_2.height)
jerry_2.height = 175
print(PersonNew.height, tom_2.height, jerry_2.height)
tom_2.height += 10
print(PersonNew.height, tom_2.height, jerry_2.height)
PersonNew.height += 15
print(PersonNew.height, tom_2.height, jerry_2.height)
PersonNew.weight = 70
print(PersonNew.weight, tom_2.weight, jerry_2.weight)

print(PersonNew.__dict__, tom_2.__dict__, jerry_2.__dict__, sep="\n")
print(tom_2.weight)
print(tom_2.__dict__['height'])



