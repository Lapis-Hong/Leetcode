#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/29
"""Prob 19. Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Description:
    Given a linked list, remove the n-th node from the end of list and return its head.
    
    Example:
    Given linked list: 1->2->3->4->5, and n = 2.
    After removing the second node from the end, the linked list becomes 1->2->3->5.
    Note:
    Given n will always be valid.
    
    Follow up:
    Could you do this in one pass?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    link_list = []
    while head:
        link_list.append(head.val)
        head = head.next
    link_list.pop(len(link_list)-n)
    return link_list


def removeNthFromEnd2(head, n):
    """Using two pointers"""
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head