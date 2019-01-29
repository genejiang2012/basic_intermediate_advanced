#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# format
res = "{}  {}  {}".format('python', 5, 'great PL')
res2 = "{1} {0} {1}".format('python', 5, 'great pl')
res3 = "{name} {age} {description}".format(
    name='python', age=5, description='great pl')
print(res)
print(res2)
print(res3)

# split

name = 'root:x:0:0::/root:/bin/bash'
print(name.split(':'))  # 默认分隔符为空格
name = 'C:/a/b/c/d.txt'  # 只想拿到顶级目录
print(name.split('/', 1))
