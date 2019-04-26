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

    def __init__(self, name, age=18, height=170):
        self.name = name
        self.__age = age
        self._height = height

    def grow_up(self, i=1):
        """TODO: Docstring for grow_up.

        :i: TODO
        :returns: TODO

        """
        if i > 1 and i <= 150:
            self.__age += i

    def get_age(self):
        return self.__age

    def _get_name(self):
        return self.name

    def __get_height(self):
        return self._height

    def get_score(self):
        ret={"English":78, "Chinese":86, "History":77}
        return reth


if __name__ == '__main__':
    Person_first = Person('Tom')
    Person_first.grow_up(151)
    print(Person_first.get_age())
    print(Person_first.__dict__)
    Person_first._Person__age = 151
    print(Person_first.get_age())
    print(Person_first._height)
    print(Person_first.__dict__)
    print(Person.__dict__)
    print(Person_first._get_name())
    # print(Person_first.__get_height())
    print(Person_first._Person__get_height())