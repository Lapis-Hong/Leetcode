#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/21
"""Prob 142. Linked List Cycle II

https://leetcode.com/problems/linked-list-cycle-ii/description/

Description:

    Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
    
    Note: Do not modify the linked list.
    
    Follow up:
    Can you solve it without using extra space?

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def detectCycle(head):
    """Floyd’s cycle detection algorithm, 
    also known as the hare-tortoise algorithm.
    :type head: ListNode
    :rtype: ListNode
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    while head != slow:
        slow = slow.next
        head = head.next
    return head

