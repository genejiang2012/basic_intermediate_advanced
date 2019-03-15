#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: FP_classmethod_staticmethod.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 

"""

class Demo(object):

    """Docstring for Demo. """

    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args


if __name__ == "__main__":
    print(Demo.klassmeth())
    print(Demo.klassmeth('spam'))
    print(Demo.statmeth())
    print(Demo.statmeth('spam'))
