#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: unpack.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""

p = (4, 5)
a, b = p
print("a value is {} and b value is {}".format(a, b))

a, b = b, a
print("a value is {} and b value is {}".format(a, b))

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print("name is {}, shares is {}, price is {} and date is {}".format(name,
                        shares, price, date))

data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print("shares is {}, price is {}".format(shares, price))
