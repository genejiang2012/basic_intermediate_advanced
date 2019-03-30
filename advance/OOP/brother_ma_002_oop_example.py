#!/usr/bin/env python4
# -*- coding: utf-8 -*-

"""
File: brother_ma_002_oop_example.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""


class Person(object):
    """docstring for Person"""

    def define_nomal_method():
        print("normal")
        return 1

    def method(self):
        print("{}'s method'".format(self))

    @classmethod
    def define_class_method(cls):
        print("class={0.__name__} {0}".format(cls))
        cls.height = 180

    @staticmethod
    def define_static_method():
        print(Person.height)


print("~~~~~~~~~~~~~~~~~~~~Access to Class~~~~~~~~~~~~~~~~~~~")
print(1, Person.define_nomal_method())
print(2, Person.method)
print(3, Person.define_class_method())
print(4, Person.define_static_method())
print(Person.__dict__)
print("~~~~~~~~~~~~~~~~~~~Access to instance~~~~~~~~~~~~~~~~~")
print("tom----------")
tom = Person()
# print(1, tom.define_nomal_method())
print(2, tom.method())
print(3, tom.define_class_method())
print(4, tom.define_static_method())
