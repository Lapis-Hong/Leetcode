#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/5/16
"""Prob 179. Largest Number

https://leetcode.com/problems/largest-number/description/

Description:
    Given a list of non negative integers, arrange them such that they form the largest number.
    
    Example 1:
    Input: [10,2]
    Output: "210"
    Example 2:
    
    Input: [3,30,34,5,9]
    Output: "9534330"
    Note: The result may be very large, so you need to return a string instead of an integer.

"""


def largestNumber(nums):
    comp = lambda a, b: 1 if a+b > b+a else -1 if a+b < b+a else 0
    nums = map(str, nums)
    nums.sort(cmp=comp, reverse=True)
    largest_num = ''.join(nums)
    return '0' if largest_num[0] == '0' else largest_num

