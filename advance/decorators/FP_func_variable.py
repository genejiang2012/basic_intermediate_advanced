#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: PF_func_variable.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""

from dis import dis

b = 6


def func(a):
    global b
    print(a)
    print(b)
    b = 9


if __name__ == "__main__":
    func(3)
    print(b)
    print(dis(func))
