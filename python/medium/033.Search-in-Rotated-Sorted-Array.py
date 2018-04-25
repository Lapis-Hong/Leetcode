#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/25
"""Prob 33. Search in Rotated Sorted Array

https://leetcode.com/problems/search-in-rotated-sorted-array/description/

Description:
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
    (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
    You are given a target value to search. If found in the array return its index, otherwise return -1.
    You may assume no duplicate exists in the array. 
    Your algorithm's runtime complexity must be in the order of O(log n).
    
    Example 1: 
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4
    Example 2:
    
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1
"""


def search(nums, target):
    if not nums:
        return -1

    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) / 2
        if target == nums[mid]:
            return mid

        if nums[low] <= nums[mid]:  # low-mid sorted
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:  # mid-high sorted
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


if __name__ == '__main__':
    print(search([4, 5, 6, 7, 0, 1, 2], 0))