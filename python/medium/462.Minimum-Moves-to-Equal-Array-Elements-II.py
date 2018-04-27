#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/27
"""Prob 462. Minimum Moves to Equal Array Elements II

https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/

Description:
    Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, 
    where a move is incrementing a selected element by 1 or decrementing a selected element by 1.
    You may assume the array's length is at most 10,000.
    
    Example:
    Input:
    [1,2,3]
    Output:
    2
    Explanation:
    Only two moves are needed (remember each move increments or decrements one element): 
    [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
"""


def minMoves2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    median = nums[len(nums) // 2]
    moves = 0
    for n in nums:
        moves += abs(n - median)
    return moves


if __name__ == '__main__':
    print(minMoves2([1, 2, 3]))