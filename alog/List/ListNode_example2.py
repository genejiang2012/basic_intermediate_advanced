#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: ListNode_example2.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: use the list to create node
"""


class SingleNode(object):
    """Docstring for SingleNode. """

    def __init__(self, data, next=None):
       self.data = data 
       self.next = next

    def __repr__(self):
        return repr(self.data)


class LinkedList(object):
    """Docstring for LinkedList. """

    def __init__(self):
        self.head = None
        self.tail = None
        self.items = []

    def append(self, item):
        node = SingleNode(item)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

        self.items.append(node)
        return self

    def traversal(self):
        cur_node = self.head
        while cur_node:
            yield cur_node
            cur_node = cur_node.next

    def get_item(self, index):
        return self.items[index]


if __name__ == "__main__":
    ll = LinkedList()
    ll.append('abc')
    ll.append(2)
    ll.append(3).append(4)
    ll.append('def')

    print(ll.head, ll.tail)

    for item in ll.traversal():
        print(item)

    for i in range(len(ll.items)):
        print(ll.get_item(i))

