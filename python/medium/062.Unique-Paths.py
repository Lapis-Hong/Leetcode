#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/5/9
"""Prob 62.Unique Paths

https://leetcode.com/problems/unique-paths/description/

Description:
    
    A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
    The robot can only move either down or right at any point in time. 
    The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
    How many possible unique paths are there?
    Above is a 7 x 3 grid. How many possible unique paths are there?
    Note: m and n will be at most 100.
    
    Example 1:
    Input: m = 3, n = 2
    Output: 3
    Explanation:
    From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Right -> Down
    2. Right -> Down -> Right
    3. Down -> Right -> Right
    Example 2:
    Input: m = 7, n = 3
    Output: 28
"""
import math


def uniquePaths(m, n):
    """Using math
    :type m: int
    :type n: int
    :rtype: int
    """
    return math.factorial(m-1 + n-1) / (math.factorial(n-1) * math.factorial(m-1))


def uniquePaths2(m, n):
    """Using DP"""
    dp = [[1 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    return dp[-1][-1]
