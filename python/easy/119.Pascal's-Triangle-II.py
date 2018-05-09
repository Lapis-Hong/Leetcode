#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/5/4
"""Prob 119. Pascal's Triangle II

https://leetcode.com/problems/pascals-triangle-ii/description/

Description:
    Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
    Note that the row index starts from 0. 
    In Pascal's triangle, each number is the sum of the two numbers directly above it.
    
    Example:
    Input: 3
    Output: [1,3,3,1]
    Follow up:
    Could you optimize your algorithm to use only O(k) extra space?
"""


# At Nth row, each k-th element is determined by a well-known formula: C(n, k) = n! / (k!*(n-k)!).
# A row in Pascal triangle is always symmetric, so we fill up two elements at each loop iteration
def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    row = [1]
    for i in range(rowIndex):
        row = [1] + [row[j] + row[j + 1] for j in range(len(row) - 1)] + [1]
    return row


def getRow2(rowIndex):
    """O(k) Space,  iteratively update the array from the end to the beginning.
    """
    res = [0 for _ in range(rowIndex+1)]
    res[0] = 1
    for i in range(1, rowIndex+1):
        for j in range(i, 0, -1):
            res[j] += res[j-1]
    return res


if __name__ == '__main__':
    print(getRow(3))
    print(getRow2(3))

