# !/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 19:08
# @Author  : Gene Jiang
# @File    : learning_jmespath.py
# @Description:

import jmespath

b = {'a': {'b': {'c': {'d': 'value'}}}}

result = jmespath.search("a.b.c.d", b)
print(result)

local_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_result = jmespath.search('[0:3]', local_list)
print(list_result)
