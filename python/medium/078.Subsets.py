#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/5/10
"""Prob 78. Subsets

https://leetcode.com/problems/subsets/description/

Description:
    Given a set of distinct integers, nums, return all possible subsets (the power set).
    Note: The solution set must not contain duplicate subsets.
    
    Example:
    Input: nums = [1,2,3]
    Output:
    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]
"""


def subsets(nums):
    """Iterative
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = [[]]
    for n in nums:
        res += [item + [n] for item in res]
    return res


def subsets1(nums):
    """DFS"""
    def dfs(nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            dfs(nums, i + 1, path + [nums[i]], res)
    res = []
    dfs(nums, 0, [], res)
    return res

if __name__ == '__main__':
    print(subsets([1,2,3]))
    print(subsets1([1,2,3]))

