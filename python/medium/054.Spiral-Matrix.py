#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/5/6
"""Prob 54. Spiral Matrix

https://leetcode.com/problems/spiral-matrix/description/

Description:

    Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
    
    Example 1:
    Input:
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    Output: [1,2,3,6,9,8,7,4,5]
    Example 2:
    Input:
    [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9,10,11,12]
    ]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


def spiralOrder(matrix):
    """Take the first row plus the spiral order of the rotated remaining matrix. Inefficient for large matrices"""
    return matrix and list(matrix.pop(0)) + spiralOrder(zip(*matrix)[::-1])


def spiralOrder2(matrix):
    def spiral_coords(r1, c1, r2, c2):
        for c in range(c1, c2 + 1):
            yield r1, c
        for r in range(r1 + 1, r2 + 1):
            yield r, c2
        if r1 < r2 and c1 < c2:
            for c in range(c2 - 1, c1, -1):
                yield r2, c
            for r in range(r2, r1, -1):
                yield r, c1

    if not matrix:
        return []
    ans = []
    r1, r2 = 0, len(matrix) - 1
    c1, c2 = 0, len(matrix[0]) - 1
    while r1 <= r2 and c1 <= c2:
        for r, c in spiral_coords(r1, c1, r2, c2):
            ans.append(matrix[r][c])
        r1 += 1
        r2 -= 1
        c1 += 1
        c2 -= 1
    return ans


def spiralOrder3(matrix):
    if not matrix or not matrix[0]:
        return []
    ans = []
    m, n = len(matrix), len(matrix[0])
    u, d, l, r = 0, m - 1, 0, n - 1
    while l < r and u < d:
        ans.extend([matrix[u][j] for j in xrange(l, r)])
        ans.extend([matrix[i][r] for i in xrange(u, d)])
        ans.extend([matrix[d][j] for j in xrange(r, l, -1)])
        ans.extend([matrix[i][l] for i in xrange(d, u, -1)])
        u, d, l, r = u + 1, d - 1, l + 1, r - 1
    if l == r:
        ans.extend([matrix[i][r] for i in xrange(u, d + 1)])
    elif u == d:
        ans.extend([matrix[u][j] for j in xrange(l, r + 1)])
    return ans


if __name__ == '__main__':
    print(spiralOrder([
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]))