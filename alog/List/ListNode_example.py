#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: ListNode_example.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""


class ListNode(object):
    """Docstring for ListNode. """

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

    def append(self, item):
        node = ListNode(item)
        if self.head is None:   # This list is empty
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        
        return self

    def traversal(self):
        cur_node = self.head
        while cur_node:
            yield cur_node
            cur_node = cur_node.next


if __name__ == "__main__":
    a = ListNode(11)
    b = ListNode(53)
    c = ListNode(59)
    a.next = b
    b.next = c
    print(a.data)
    print(a.next.data)
    print(a.next.next.data)
     
    ll = LinkedList()
    ll.append('abc')
    ll.append(1)
    ll.append('def')

    print(ll.head, ll.tail)

    for item in ll.traversal():
        print(item)
        

