#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/5/16
"""Prob 11. Container With Most Water

https://leetcode.com/problems/container-with-most-water/description/

Description:

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, 
such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""


def maxArea(height):
    """Two Pointer Approach
    :type height: List[int]
    :rtype: int
    """
    max_area, l, r = 0, 0, len(height) - 1
    while l < r:
        max_area = max(max_area, min(height[l], height[r]) * (l - r))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area