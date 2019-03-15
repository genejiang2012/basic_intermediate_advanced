#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: DoublyLinkList_example.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description:
"""


class DlistNode(object):

    """Docstring for DlistNode. """

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return "({} <=={} ==>{})".format(self.prev.data if self.prev else None, 
                                         self.data, 
                                         self.next.data if self.next else None)


class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, item):
        node = DlistNode(item)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        return self


if __name__ == "__main__":
    a = DlistNode('11')
    b = DlistNode('77')
    c = DlistNode('88')
    a.next = b
    b.prev = a
    b.next = c
    c.prev = b

    print(a, b, c)

    dll = DLinkedList()
    dll.append('1')
    dll.append('3')

    print(dll.head, dll.tail)


    


