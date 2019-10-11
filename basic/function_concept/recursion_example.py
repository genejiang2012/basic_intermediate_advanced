#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: recursion_example.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: some exmpales for decorator 
"""
import time


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    start_time = time.time()
    print(fib(50))
    cost_time = time.time() - start_time
    print(cost_time)
