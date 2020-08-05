#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: my_stack.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: stack example 
"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        return self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def tranversal(self):
        for item in self.items:
            print(item)


def par_checker(symbol_string : list):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]

        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()

        index += 1

    if s.is_empty() and balanced:
        return True
    else:
        return False


local_string = "{ [ ( ( ) ) ] }"
transfer_list = local_string.split(" ")

print(par_checker(transfer_list))
