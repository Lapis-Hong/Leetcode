#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/5/5
"""Prob 46. Permutations

https://leetcode.com/problems/permutations/description/

Description:
    Given a collection of distinct integers, return all possible permutations.
    
    Example:
    Input: [1,2,3]
    Output:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
"""


# DFS
def permute(nums):
    """DFS
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def dfs(nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in xrange(len(nums)):
            dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)

    res = []
    dfs(nums, [], res)
    return res


def permute2(nums):
    """Iterative"""
    perms = [[]]
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in xrange(len(perm)+1):
                new_perms.append(perm[:i] + [n] + perm[i:])
        perms = new_perms
    return perms


def permut3(nums):
    """Recursive"""
    return [[n] + p
            for i, n in enumerate(nums)
            for p in permute(nums[:i] + nums[i+1:])] or [[]]


if __name__ == '__main__':
    print(permute([1,2,3]))