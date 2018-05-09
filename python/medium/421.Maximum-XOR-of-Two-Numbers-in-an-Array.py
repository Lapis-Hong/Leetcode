#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/5/2
"""Prob 421. Maximum XOR of Two Numbers in an Array

https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/

Description:
    Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.
    Find the maximum result of ai XOR aj, where 0 ≤ i, j < n. 
    Could you do this in O(n) runtime?
    
    Example:
    Input: [3, 10, 5, 25, 2, 8] 
    Output: 28
    Explanation: The maximum result is 5 ^ 25 = 28.
"""


def findMaximumXOR(nums):
    res = 0
    for i in range(32)[::-1]:
        res <<= 1
        prefixes = {num >> i for num in nums}
        res += any(res^1 ^ p in prefixes for p in prefixes)
    return res


if __name__ == '__main__':
    print(findMaximumXOR([3, 10, 5, 25, 2, 8]))