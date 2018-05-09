#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/5/4
"""Prob 60. Permutation Sequence

https://leetcode.com/problems/permutation-sequence/description/

Description:
    The set [1,2,3,...,n] contains a total of n! unique permutations.  
    By listing and labeling all of the permutations in order, we get the following sequence for n = 3:  
    "123"
    "132"
    "213"
    "231"
    "312"
    "321"
    Given n and k, return the kth permutation sequence.
    
    Note:
    Given n will be between 1 and 9 inclusive.
    Given k will be between 1 and n! inclusive.
    Example 1: 
    Input: n = 3, k = 3
    Output: "213"
    Example 2: 
    Input: n = 4, k = 9
    Output: "2314"
"""
import math


def getPermutation(n, k):
    nums = range(1, n+1)
    res = ''
    k -= 1
    while n > 0:
        n -= 1
        # get the index of current digit
        index, k = divmod(k, math.factorial(n))
        res += str(nums[index])
        # remove handled number
        nums.remove(nums[index])
    return res


if __name__ == '__main__':
    print(getPermutation(4, 9))
