#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: mylog.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/yourname
Description: 
"""

import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG) 


def foo(): 
    print("I am inside foo.")


def logged(func, *args, **kwargs):
    logger = logging.getLogger()

    def new_func(*args, **kwargs):
        logger.debug("calling {} with args {} and kwarges {}".format(
                    func.__name__, args, kwargs))
        return func(*args, **kwargs)
    return new_func


@logged
def bar(args='test'):
    print("I am inside the bar {}.".format(args))


def deco(func):
    def inner():
        print('running inner()')
    return inner


@deco
def target():
    print('running target()')


if __name__ == "__main__":
    print(bar("test"))
    print(foo())
    print(target)
    print(target())
