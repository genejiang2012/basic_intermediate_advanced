#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: brother_ma_004_oop_property.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""


class Person(object):

    """Docstring for Person. """

    def __init__(self, name, age=18):
        """initialize the class"""
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @age.deleter
    def age(self):
        # del self.__age
        print('del')


tom = Person('Tom')
print(tom.age)
tom.age = 20
print(tom.age)
del tom.age


