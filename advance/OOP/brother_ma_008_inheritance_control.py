#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: brother_ma_008_inheritance_control.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""


class Animal(object):
    __COUNT = 100
    HEIGHT = 0

    def __init__(self, age, weight, height):
        self.__COUNT += 1
        self.age = age
        self.__weight = weight
        self.height = height

    def eat(self):
        print('{} eats'.format(self.__class__.__name__))

    def __get_weight(self):
        print(self.__weight)

    @classmethod
    def shout_count1(cls):
        print(cls.__COUNT)

    @classmethod
    def __shout_count2(cls):
        print(cls.__COUNT)
   
    def shout_count3(self):
        print(self.__COUNT)


class Cat(Animal):
    NAME = 'CAT'
    __COUNT = 200

    @property
    def count(self):
        return self.__COUNT


# c = Cat()  # fail to initialize
c = Cat(3, 5, 15)
c.eat()
print(c.HEIGHT)
# print(c.__COUNT) # private cannot be access
# c.__show_height()
c.shout_count1()
# c.__shout_count2() # private cannot be access
c.shout_count3()
print(c.NAME)
print(c.count)
print('{}'.format(Animal.__dict__))
print('{}'.format(Cat.__dict__))
print(c.__dict__)
print(c.__class__.mro())
