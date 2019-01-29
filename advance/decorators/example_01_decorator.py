#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: example_01_decorator.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""


def check_is_admin(f):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception('This user is not allowed to get food!')
        return f(*args, **kwargs)

    return wrapper


class Store(object):
    """Docstring for Store. """

    @check_is_admin
    def get_food(self, username, food):
        return self.storage.get(food)

    @check_is_admin
    def put_food(self, username, food):
        return self.storage.put(food)


if __name__ == '__main__':
    my_store = Store()
    my_food = my_store.get_food(admin='admin', food='Juice')
    print(my_food)