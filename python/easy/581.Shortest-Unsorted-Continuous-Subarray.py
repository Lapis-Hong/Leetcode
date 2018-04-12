#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/12
"""Prob 581. Shortest Unsorted Continuous Subarray

https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/

Description:
    Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
    
    You need to find the shortest such subarray and output its length.
    
    Example 1:
    Input: [2, 6, 4, 8, 10, 9, 15]
    Output: 5
    Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
    Note:
    Then length of the input array is in range [1, 10,000].
    The input array may contain duplicates, so ascending order here means <=.
"""

# using sorting
def findUnsortedSubarray(nums):
    """Time complexity: O(nlogn); Space complexity: O(n)
    :type nums: List[int]
    :rtype: int
    """
    sorted_nums = sorted(nums)
    start = len(nums)
    end = 0
    for i in range(len(nums)):
        if nums[i] != sorted_nums[i]:
            start = min(start, i)
            end = max(end, i)
    return end - start + 1 if end >= start else 0


def findUnsortedSubarray2(nums):
    """Using sorting version"""
    is_same = [a == b for a, b in zip(nums, sorted(nums))]
    return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)


# find start index: from right to left, bigger than min element of its right side
# find end index: from left to right, smaller than max element of its left side
def findUnsortedSubarray3(nums):
    """O(n) and O(1)"""
    n = len(nums)
    start = -1
    end = -2
    min_ = nums[-1]
    max_ = nums[0]
    for i in range(1, n-1):
        max_ = max(max_, nums[i])
        min_ = min(min_, nums[n-i-1])
        if nums[i] < max_:
            end = i
        if nums[n-i-1] > min_:
            start = n-i-1
    return end - start + 1


if __name__ == '__main__':
    print(findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
    print(findUnsortedSubarray3([2, 6, 4, 8, 10, 9, 15]))


