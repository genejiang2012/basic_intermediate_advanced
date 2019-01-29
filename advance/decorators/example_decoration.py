#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: example_decoration.py
Author: Gene Jiang
Email: zhengrong.jiang@chiefclouds.com
Github: https://github.com/yourname
Description: Chapter 9 from <<The Hacker's Guide to Python>>
"""

_functions = {}


def register(f):
    global _functions

    _functions[f.__name__] = f
    return f


@register
def foo():
    return 'bar'


@register
def bar():
    return 'bar2'


def check_is_admin(username):
    if username != 'admin':
        raise Exception("This user is not allowed to get food.")



@check_if_admin
def get_food(self, username, food):
     return self.storage.get(food)



