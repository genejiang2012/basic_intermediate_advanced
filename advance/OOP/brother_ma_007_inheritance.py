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
    x = 123

    def __init__(self, name):
        self._name = name
        self.__age = 10

    def shout(self):
        print('Animal shouts')
        # print('{} shouts'.format(self.__class__.__name__))

    @property
    def name(self):
        return self._name


class Cat(Animal):
    x = 'cat'

    def __init__(self, name):
        Animal.__init__(self, name)
        self._name = "cat"+name
        self.__age = 20


    def shout(self):
        print('Cat shouts')


class Garfied(Cat):
    pass


class Dog(Animal):
    def run(self):
        print('Dog run')


tom = Garfied('tom')
print(tom.name)
print(tom.shout())
print(tom.__dict__)
print(Garfied.__dict__)
print(Cat.__dict__)
print(Animal.__dict__)

# a = Animal('monster')
# a.shout()
#
#
# cat = Cat('garfield')
# cat.shout()
# print(cat.name)
# print(cat.__age)
# print(cat.__dict__)
#
#
# dog = Dog('ahuang')
# dog.shout()
# print(dog.name)
# print('cat.mro = {}'.format(cat.__class__.__mro__))
# print('cat.base = {}'.format(cat.__class__.__bases__))


