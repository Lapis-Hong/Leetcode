#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/26
"""Prob 18. 4Sum

https://leetcode.com/problems/4sum/description/

Description:

    Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums 
    such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
    Note:
    The solution set must not contain duplicate quadruplets.

    Example: 
    Given array nums = [1, 0, -1, 0, -2, 2], and target = 0. 
    A solution set is:
    [
      [-1,  0, 0, 1],
      [-2, -1, 1, 2],
      [-2,  0, 0, 2]
    ]
"""


def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()
    n = len(nums)
    for i in range(0, n - 3):
        if nums[i] > target / 4:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i + 1, n - 2):
            s = nums[i] + nums[j]
            if s > target / 2:
                break
            if nums[j] == nums[j-1]:
                continue
            l = j + 1
            h = n - 1
            while l < h:
                if nums[l] + nums[h] > target - s:
                    h -= 1
                elif nums[l] + nums[h] < target - s:
                    l += 1
                else:
                    res.append([nums[i], nums[j], nums[l], nums[h]])
                    l += 1
                    h -= 1
                    while l < h and nums[l] == nums[l - 1]:  # pass same element
                        l += 1
                    while l < h and nums[h] == nums[h + 1]:
                        h -= 1
    return res


if __name__ == '__main__':
    print(fourSum([1, 0, -1, 0, -2, 2], 0))