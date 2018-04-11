#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/11
"""Prob 507. Perfect Number

https://leetcode.com/problems/perfect-number/description/

Description:
    We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
    
    Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
    Example:
    Input: 28
    Output: True
    Explanation: 28 = 1 + 2 + 4 + 7 + 14
    Note: The input number n will not exceed 100,000,000. (1e8)
"""


def checkPerfectNumber(num):
    """
    :type num: int
    :rtype: bool
    """
    if num <= 0:
        return False
    s = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            s += (i + num / i)
    if int(num ** 0.5) ** 2 == num:  # remove duplicate divisors
        s -= int(num ** 0.5)
    return s == 2 * num


if __name__ == '__main__':
    print(checkPerfectNumber(23444))