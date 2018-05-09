#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/30
"""Prob 766. Toeplitz Matrix

https://leetcode.com/problems/toeplitz-matrix/description/

Description:
    A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
    Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
      
    Example 1:
    Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    Output: True
    Explanation:
    1234
    5123
    9512
    
    In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]", and in each diagonal all elements are the same, so the answer is True.
    Example 2:
    Input: matrix = [[1,2],[2,2]]
    Output: False
    Explanation:
    The diagonal "[1, 2]" has different elements.
    Note:
    
    matrix will be a 2D array of integers.
    matrix will have a number of rows and columns in range [1, 20].
    matrix[i][j] will be integers in range [0, 99].
"""


def isToeplitzMatrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: bool
    """
    nrow = len(matrix)
    ncol = len(matrix[0])
    for i in range(nrow - 1):
        for j in range(ncol - 1):
            if matrix[i + 1][j + 1] != matrix[i][j]:
                return False
    return True


def isToeplitzMatrix2(m):
    return all(m[i][j] == m[i+1][j+1] for i in range(len(m)-1) for j in range(len(m[0])-1))


if __name__ == '__main__':
    print(isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))