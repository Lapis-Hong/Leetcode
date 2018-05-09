#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/5/2
"""Prob 780. Reaching Points

https://leetcode.com/problems/reaching-points/description/

Description:

    A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).
    Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.
    
    Examples:
    Input: sx = 1, sy = 1, tx = 3, ty = 5
    Output: True
    Explanation:
    One series of moves that transforms the starting point to the target is:
    (1, 1) -> (1, 2)
    (1, 2) -> (3, 2)
    (3, 2) -> (3, 5)
    
    Input: sx = 1, sy = 1, tx = 2, ty = 2
    Output: False
    
    Input: sx = 1, sy = 1, tx = 1, ty = 1
    Output: True
    
    Note:
    sx, sy, tx, ty will all be integers in the range [1, 10^9].
"""


# Basic idea:
# If we start from sx,sy, it will be hard to find tx, ty.
# If we start from tx,ty, we can find only one path to go back to sx, sy.
# If sx,sy occurs in the path of Euclidean method to get GCD (by subtracting lesser value from greater value) of tx,ty,
# then return true.
def reachingPoints(sx, sy, tx, ty):
    while sx < tx and sy < ty:
        tx, ty = tx % ty, ty % tx
    return sx == tx and (ty - sy) % sx == 0 or sy == ty and (tx - sx) % sy == 0
