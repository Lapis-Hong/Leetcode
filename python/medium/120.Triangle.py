#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/24
"""Prob 120. Triangle

https://leetcode.com/problems/triangle/description/

Description:
    Given a triangle, find the minimum path sum from top to bottom. 
    Each step you may move to adjacent numbers on the row below.
    For example, given the following triangle
    
    [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
    
    Note:
    Bonus point if you are able to do this using only O(n) extra space, 
    where n is the total number of rows in the triangle.
"""


def minimumTotal(triangle):
    """Bottom-up DP, O(n) space
    the min pathsum at the jth node on the ith row would be the lesser of the pathsums 
    of its two children plus the value of itself.
    minpath[i][j] = min( minpath[i+1][j], minpath[i+1][j+1]) + triangle[i][j];
    Since the row minpath[k+1] would be useless after minpath[k] is computed, 
    we can simply set minpath as a 1D array, and iteratively update itself:
    For the ith row: 
    minpath[j] = min( minpath[j], minpath[j+1]) + triangle[i][j]
    """
    if not triangle:
        return
    res = triangle[-1]
    for i in xrange(len(triangle) - 2, -1, -1):
        for j in xrange(len(triangle[i])):  # Check its every 'node'
            res[j] = min(res[j], res[j + 1]) + triangle[i][j]
    return res[0]


def minimumTotal1(triangle):
    """O(n*n/2) space, top-down 
    res: store each node ans."""
    if not triangle:
        return
    res = [[0 for _ in xrange(len(row))] for row in triangle]
    res[0][0] = triangle[0][0]
    for i in xrange(1, len(triangle)):
        for j in xrange(len(triangle[i])):
            if j == 0:
                res[i][j] = res[i - 1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                res[i][j] = res[i - 1][j - 1] + triangle[i][j]
            else:
                res[i][j] = min(res[i - 1][j - 1], res[i - 1][j]) + triangle[i][j]
    return min(res[-1])


# Modify the original triangle, top-down
def minimumTotal2(triangle):
    if not triangle:
        return
    for i in xrange(1, len(triangle)):
        for j in xrange(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
    return min(triangle[-1])


# Modify the original triangle, bottom-up
def minimumTotal3(triangle):
    if not triangle:
        return
    for i in xrange(len(triangle) - 2, -1, -1):
        for j in xrange(len(triangle[i])):
            triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
    return triangle[0][0]


if __name__ == '__main__':
    print(minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))