#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: FP_nested_func.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""


def outer():
    x=1
    def inner():
        print(x)
        print("inner locals %s" % locals())
    print("outer locals %s" % locals())
    return inner

       

if __name__ == '__main__':
    func=outer()
    print(func)
    print(func.__closure__)
    func()
