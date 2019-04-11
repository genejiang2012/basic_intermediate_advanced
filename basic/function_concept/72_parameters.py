#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
"""
File: 72_parameters.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""


# position parameters

def define_fn(x=10, y=11, *args, **kwargs):
    print(x, y)
    print(args)
    print(kwargs)


define_fn(1, 2, 3, 4, 5, i=10, j=12)


# Keyword-only parameters


def fn(*args, x=2, y=3):
    print(args)
    print("x={0}, y={1} ".format(x, y))


fn(1, 2, 3)  # error:fn() missing 2 required keyword-only arguments: 'x' and 'y'
fn(1, x=2, y=3)

print("-" * 80)


def add(*iter):
    result = 0
    for x in iter:
        result += x
    return result


print(add(1, 2, 3))
print(add(*[1, 2, 3]))
print(add(*range(10)))

print("-" * 80)


def input_double_values(*args):
    print(args)
    return max(args), min(args)


print(*input_double_values(*[random.randint(10, 20) for _ in range(10)]))

print("-" * 80)


def showlist():
    return (1, 3, 5)


print(showlist())


print("-" * 80)


def outer1():
    o = 65

    def inner():
        o = 97
        print("innter {} ".format(o))
        print(chr(o))

    print("outer{}".format(o))

    inner()


outer1()

print("-" * 80)


def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


print(minimum(1, 5, 2, -5, 10))  # Returns -5
print(minimum(1, 5, 2, -5, 10, clip=0))  # Returns 0
