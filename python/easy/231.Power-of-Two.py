#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/5/2
"""Prob 231. Power of Two

https://leetcode.com/problems/power-of-two/description/

Description:
    Given an integer, write a function to determine if it is a power of two.
"""


def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0:
        return False
    while n > 2:
        if n % 2 == 0:
            n /= 2
        else:
            return False
    return True


def isPowerOfTwo2(n):
    """Power of 2 means only one bit of n is '1', 
    so use the trick n&(n-1)==0 to judge whether that is the case"""
    return n > 0 and not (n & n-1)


if __name__ == '__main__':
    print(isPowerOfTwo(16))
    print(isPowerOfTwo2(16))