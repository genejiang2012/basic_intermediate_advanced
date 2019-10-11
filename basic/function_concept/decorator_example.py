#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: decorator_example.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: some exmpales for decorator 
"""


def add1(x, y, z):
    return x + y + z


def old_logger(fn):
    print('begin')
    x = fn(4, 5)
    print('end')
    return x


def new_logger(fn, *args, **kwargs):
    print('begin')
    x = fn(*args, **kwargs)
    print('end')
    return x


def copy_properties(src):
    def _copy(dst):
        dst.__name__ = src.__name__
        dst.__doc__ = src.__doc__
        return dst

    return _copy


def logger(fn):
    @copy_properties(fn)
    def wrapper(*args, **kwargs):
        """
        I a wrapper
        """
        print('begin')
        x = fn(*args, **kwargs)
        print('end')
        return x

    return wrapper


@logger
def add(x, y):
    """
    This is a function for add
    """
    return x + y


print(logger(add))

print(new_logger(add, 10, 20))
print(new_logger(add1, 10, 20, z=30))
print(logger(add)(5, y=50))
print(add(45, 40))

print("name = {}, doc={}".format(add.__name__, add.__doc__))
