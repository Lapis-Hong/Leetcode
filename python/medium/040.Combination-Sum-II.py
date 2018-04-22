#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/22
"""Prob 40. Combination Sum II

https://leetcode.com/problems/combination-sum-ii/description/

Description:
    Given a collection of candidate numbers (candidates) and a target number (target), 
    find all unique combinations in candidates where the candidate numbers sums to target.
    Each number in candidates may only be used once in the combination.
    
    Note:
    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.
    
    Example 1:
    Input: candidates = [10,1,2,7,6,1,5], target = 8,
    A solution set is:
    [ [1, 7],
      [1, 2, 5],
      [2, 6],
      [1, 1, 6]
    ]
    Example 2:
    Input: candidates = [2,5,2,1,2], target = 5,
    A solution set is:
    [ [1,2,2],
      [5]
    ]
"""


def combinationSum(candidates, target):
    """DP"""
    candidates.sort()
    # dp[i] store the result of target = i
    dp = [set() for _ in xrange(target + 1)]
    dp[0].add(())
    for num in candidates:
        for t in xrange(target, num - 1, -1):
            for prev in dp[t - num]:
                dp[t].add(prev + (num,))
    return list(dp[-1])


def combinationSum2(candidates, target):
    """DFS, recursive"""
    def search(candidates, start, target):
        if target == 0:
            return [[]]
        res = []
        for i in xrange(start, len(candidates)):
            if i != start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            for r in search(candidates, i + 1, target - candidates[i]):
                res.append([candidates[i]] + r)
        return res

    candidates.sort()
    return search(candidates, 0, target)


if __name__ == '__main__':
    print(combinationSum([10, 1, 2, 7, 6, 1, 5], 8))
    print(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
