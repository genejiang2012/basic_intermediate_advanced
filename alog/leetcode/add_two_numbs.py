#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: add_two_numbs.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    """Docstring for Solution. """

    def add_two_numbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        tmp = ListNode(0)
        res = tmp
        flag = 0

        while l1 or l2:
            tmp_sum = 0
            if l1:
                tmp_sum += l1.val
                l1 = l1.next
            if l2:
                tmp_sum += l2.val
                l2 = l2.next

            tmp_res = ((tmp_sum + flag) % 10)
            flag = ((tmp_sum + flag) // 10)
            res.next = ListNode(tmp_res)
            res = res.next

        if flag:
            res.next = ListNode(1)

        res = tmp.next
        del tmp
        return res


if __name__ == '__main__':
    # Create the object
    sol = Solution()
    # define the linked list of L1
    l1 = ListNode(2)
    l1.next = l11 = ListNode(4)
    l11.next = l12 = ListNode(5)
    # define the linked list of l2
    l2 = ListNode(5)
    l2.next = l21 = ListNode(6)
    l21.next = l22 = ListNode(4)
    # get the returned values
    res = sol.add_two_numbers(l1, l2)

    # get every value
    while res:
        print(res.val)
        res = res.next
