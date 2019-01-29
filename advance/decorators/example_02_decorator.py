#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: example_02_decorator.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: the example for decorator
"""

import time
from functools import wraps
import logging


def timethis(func):
    """TODO: Docstring for timethis.
    :returns: TODO
    """
    # @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper


@timethis
def count_down(n):
    while n > 0:
        n -= 1


print(count_down(1000))
print(count_down(1000000))


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper


@decorator1
@decorator2
def add(x, y):
    return x + y


print(add(2, 3))
print(add.__wrapped__(2, 3))


print("*"*80)


def logged(level, name=None, message=None):
    """
    Add logging to a function_concept. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function_concept's module and name.
    """
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate


# Example use
@logged(logging.INFO)
def add(x, y):
    return x + y


@logged(logging.WARNING, 'example')
def spam():
    print('Spam!')

print(add(2, 3))
print(spam())