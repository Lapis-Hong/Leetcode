#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/10
"""Prob 665. Non-decreasing Array
Description:
    Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

    We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
    
    Example 1:
    Input: [4,2,3]
    Output: True
    Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
    Example 2:
    Input: [4,2,1]
    Output: False
    Explanation: You can't get a non-decreasing array by modify at most one element.
    Note: The n belongs to [1, 10,000].
"""


# The logic is to first find any inversions, and if the number of inversions is > 1,
# then we need to modify more than 1 element and hence we return False.
# Once we find an inversion,
# we have to fix either the current value or the next value appropriately so that any future inversions can be detected correctly.
def checkPossibility(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    count = 0
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            count += 1
            if i == 0:
                nums[i] = nums[i + 1]
            elif nums[i-1] <= nums[i+1]:
                nums[i] = nums[i-1]
            else:
                nums[i+1] = nums[i]
    return count <= 1


if __name__ == '__main__':
    print(checkPossibility([4, 2, 3]))
    print(checkPossibility([3, 4, 2, 3]))