#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/5/10
"""Prob 73. Set Matrix Zeroes

https://leetcode.com/problems/set-matrix-zeroes/description/

Description:
    Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
    
    Example 1:
    Input: 
    [
      [1,1,1],
      [1,0,1],
      [1,1,1]
    ]
    Output: 
    [
      [1,0,1],
      [0,0,0],
      [1,0,1]
    ]
    Example 2:
    Input: 
    [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]
    Output: 
    [
      [0,0,0,0],
      [0,4,5,0],
      [0,3,1,0]
    ]
    Follow up: 
    A straight forward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?
"""


def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    nrow = len(matrix)
    ncol = len(matrix[0])
    zero_row, zero_col = [], []
    for i in range(nrow):
        for j in range(ncol):
            if matrix[i][j] == 0:
                zero_row.append(i)
                zero_col.append(j)
    for r in zero_row:
        matrix[r] = [0]*ncol
    for c in zero_col:
        for i in range(nrow):
            matrix[i][c] = 0


if __name__ == '__main__':
    matrix = [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]
    setZeroes(matrix)
    print(matrix)