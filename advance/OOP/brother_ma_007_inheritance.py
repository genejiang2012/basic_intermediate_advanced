#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: brother_ma_007_inheritance.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: some examples for inheritance 
"""


class Animal(object):
    def __init__(self, name):
        self._name = name

    def shout(self):
        # print('Animal shouts')
        print('{} shouts'.format(self.__class__.__name__))

    @property
    def name(self):
        return self._name


a = Animal('monster')
a.shout()


class Cat(Animal):
    # def shout(self):
    #     print('Cat shouts')
    pass


# c = Cat()
# c.shout()

cat = Cat('garfield')
cat.shout()
print(cat.name)


class Dog(Animal):
    pass


dog = Dog('ahuang')
dog.shout()
print(dog.name)


