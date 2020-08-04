#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: test.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description:
"""

from ..my_module import my_func


def test_get_true_func():
    assert my_func.MyModule.get_true() == True


def test_get_false_func():
    assert my_func.MyModule.get_false() == False
