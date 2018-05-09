#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/5/5
"""Prob 47. Permutations II

https://leetcode.com/problems/permutations-ii/description/

Description:
    Given a collection of numbers that might contain duplicates, return all possible unique permutations.
    
    Example:
    Input: [1,1,2]
    Output:
    [
      [1,1,2],
      [1,2,1],
      [2,1,1]
    ]
"""


def permuteUnique(num):
    if not num:
        return []
    num.sort()
    res = [[]]
    for n in num:
        new_res = []
        l = len(res[-1])
        for seq in res:
            for i in range(l, -1, -1):
                if i < l and seq[i] == n:
                    break
                new_res.append(seq[:i] + [n] + seq[i:])
        res = new_res
    return res


def permuteUnique2(nums):
    ans = [[]]
    for n in nums:
        ans = [l[:i]+[n]+l[i:]
               for l in ans
               for i in xrange((l+[n]).index(n)+1)]
    return ans


if __name__ == '__main__':
    print(permuteUnique([1,1,2]))