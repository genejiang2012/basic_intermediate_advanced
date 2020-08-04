#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: iter_test.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/yourname
Description: 
"""

x = 'hello'
print(dir(x))

iter_test = x.__iter__()
print(iter_test)
print(iter_test.__next__())
print(iter_test.__next__())
print(iter_test.__next__())
print(iter_test.__next__())
print(iter_test.__next__())

l = [1,2, 3]
for i in l:
    print(i)

index = 0
while index < len(l):
    print(l[index])
    index += 1

iter_l = l.__iter__()
print(iter_l.__next__())

for i in l:
    print(i)

dict_example = {'a': 1, 'b': 2}
iter_dict = dict_example.__iter__()
print(iter_dict.__next__())

