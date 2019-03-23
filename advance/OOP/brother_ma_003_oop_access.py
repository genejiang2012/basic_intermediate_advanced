#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: brother_ma_003_oop_access.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""


class Person(object):
    """docstring for Person"""
    def __init__(self, name, age=18):
        self.name = name
        self.__age = age

    def grow_up(self, i=1):
        """TODO: Docstring for grow_up.

        :i: TODO
        :returns: TODO

        """
        if i > 1 and i <= 150:
            self.__age += i

    def get_age(self):
        return self.__age


if __name__ == '__main__':
    Person_first = Person('Tom')
    Person_first.grow_up(20)
    print(Person_first.get_age())


