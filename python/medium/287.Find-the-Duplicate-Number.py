#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/21
"""Prob 287. Find the Duplicate Number

https://leetcode.com/problems/find-the-duplicate-number/description/

Description:

    Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
    
    Note:
    You must not modify the array (assume the array is read only).
    You must use only constant, O(1) extra space.
    Your runtime complexity should be less than O(n2).
    There is only one duplicate number in the array, but it could be repeated more than once.

"""


def findDuplicate(nums):
    """If we interpret nums such that for each pair of index i and value v_i,
​​    the "next" value v_j is at index v_i, 
    we can reduce this problem to cycle detection."""
    # Find the meeting point of the two runners.
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    # Find the "entrance" to the cycle.
    # slow from start, fast from meeting, then meeting again at entrance.
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr1