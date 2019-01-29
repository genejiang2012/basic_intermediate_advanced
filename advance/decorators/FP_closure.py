#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: FP_closure.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""


class Averager(object):
    """Docstring for Averager. """

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


if __name__ == "__main__":
    avg = Averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))

    avg = make_averager()
    print(avg)
    print(avg(10))
    print(avg(11))
    print(avg(20))
    print(avg.__closure__)

    scope_test()
    print("In global scope:", spam)
