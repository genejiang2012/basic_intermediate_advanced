#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: FP_highorder_func.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description:  
"""
import time


def foo():
    time.sleep(3)
    print("from foo")


def timer(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print("The excution time is %s s" % (end_time - start_time))
    return func


foo=timer(foo)
foo()


