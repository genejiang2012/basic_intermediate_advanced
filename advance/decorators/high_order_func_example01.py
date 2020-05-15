#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: high_order_func_example01.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: some example_01 for high order function
"""


def counter(base=10):
    def inc(step=1):
        nonlocal base
        base += step
        return base

    return inc


def counter_closure(base=10):
    def inc(step=1):
        print(base, step)
        return base

    return inc


def sort(iterable, reverse=False, key=lambda a, b: a < b):
    """
    sorted func defined by myself
    :returns: the iterable is sorted
    """
    ret = []
    for x in iterable:
        for i, y in enumerate(ret):
            # flag = x > y if reverse else x < y
            flag = key(x, y) if not reverse else not key(x, y)
            if flag:
                ret.insert(i, x)
                break
        else:
            ret.append(x)
    return ret


if __name__ == '__main__':
    print(counter()())
    print(counter()())
    print(sort([3, 7, 10, 5, 4], True))
    print(sorted([3, 7, 10, 5, 4], reverse=True))
    lst = [3, 7, 10, 5, 4]
    print(lst)
    print([lst.sort()])
