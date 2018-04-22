#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/22
"""Prob 128. Longest Consecutive Sequence

https://leetcode.com/problems/longest-consecutive-sequence/description/


Description:
    Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
    
    Your algorithm should run in O(n) complexity.
    
    Example:
    
    Input: [100, 4, 200, 1, 3, 2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""


def longestConsecutive(nums):
    """Using sorting
    Time complexity: O(nlgn); Space complexity: O(1)"""
    if not nums:
        return 0

    nums.sort()

    longest = 1
    current = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            if nums[i] == nums[i - 1] + 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 1

    return max(longest, current)


def longestConsecutive2(nums):
    """Using hash O(n)"""
    longest = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current = 1

            while current_num + 1 in num_set:
                current_num += 1
                current += 1
            longest = max(longest, current)

    return longest


if __name__ == '__main__':
    print(longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(longestConsecutive2([100, 4, 200, 1, 3, 2]))