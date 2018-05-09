#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/5/3
"""Prob 21. Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/description/

Description:

    Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
    
    Example:
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists1(a, b):
    if a and b:
        if a.val > b.val:
            a, b = b, a
        a.next = mergeTwoLists1(a.next, b)
    return a or b


def mergeTwoLists2(a, b):
    if not a or b and a.val > b.val:
        a, b = b, a
    if a:
        a.next = mergeTwoLists2(a.next, b)
    return a


# iteratively
def mergeTwoLists3(l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next


# recursively
def mergeTwoLists4(l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = mergeTwoLists4(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists4(l1, l2.next)
        return l2


# in-place, iteratively
def mergeTwoLists5(l1, l2):
    if None in (l1, l2):
        return l1 or l2
    dummy = cur = ListNode(0)
    dummy.next = l1
    while l1 and l2:
        if l1.val < l2.val:
            l1 = l1.next
        else:
            nxt = cur.next
            cur.next = l2
            tmp = l2.next
            l2.next = nxt
            l2 = tmp
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next