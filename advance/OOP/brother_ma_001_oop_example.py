#!/usr/bin/env python3

"""
File: brother_ma_001_oop_example.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""


class MyClass:
    """A example of class"""
    x = 'abc'

    def __init__(self):
        print("self in init={}".format(id(self)))

    def foo(self):
        return 'my class'


class Person(object):
    """Docstring for Person. """
    age = 3

    def __init__(self, name, age):
        self.name = name
        # self.age = age

    def showage(self):
        print("{} is {}".format(self.name, self.age))


        
print(MyClass)
print(MyClass())
print("="*10)
print(MyClass().__doc__)
print("="*10)

Tom = Person('Tom', 22)
Jerry = Person('Jerry', 31)
print(Tom.name, Jerry.age)
Jerry.age += 1
print(Jerry.age)
Jerry.showage()

print("="*10)

c = MyClass()
print('c = {}'.format(id(c)))
