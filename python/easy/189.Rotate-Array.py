#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/16
"""Prob 189. Rotate Array

https://leetcode.com/problems/rotate-array/description/

Description:

    Rotate an array of n elements to the right by k steps.
    
    For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
    
    Note:
    Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
    
    Hint:
    Could you do it in-place with O(1) extra space?
    
    Related problem: Reverse Words in a String II
    
    Credits:
    Special thanks to @Freezen for adding this problem and creating all test cases.
"""


def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]  # not nums = nums[n-k:] + nums[:n-k]


if __name__ == '__main__':
    nums = (1, 2, 3, 4, 5, 6, 7)
    k = 3
    rotate(nums, k)
    print(nums)

