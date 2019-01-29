#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: FP_decorators_example01.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""

registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print("running f1")


@register
def f2():
    print("running f2")


def f3():
    print("running f3")


def main():
    print("running main()")
    print('registry ->', registry)
    f1()
    f2()
    f3()


if __name__ == "__main__":
    main()

# running register(<function f1 at 0x027FBC00>)
# running register(<function f2 at 0x027FBB70>)
# running main()
# registry -> [<function f1 at 0x027FBC00>, <function f2 at 0x027FBB70>]
# running f1
# running f2
# running f3
