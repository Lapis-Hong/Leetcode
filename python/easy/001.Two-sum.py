"""Prob 1. Two Sum

https://leetcode.com/problems/two-sum/description/

Description:
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.  
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    
    Example: 
    Given nums = [2, 7, 11, 15], target = 9, 
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""


def two_sum(nums, target):
    nums.sort()
    head = 0
    tail = len(nums) - 1
    res = []
    while head < tail:
        if nums[head] + nums[tail] == target:
            res.append([head, tail])
            head += 1
            tail -= 1
        elif nums[head] + nums[tail] < target:
            head += 1
        else:
            tail -= 1
    return res


def two_sum1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)-1):
         for j in range(i+1, len(nums)):
             if nums[i] + nums[j] == target:
                 return [i, j]


def two_sum2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {v: k for k, v in enumerate(nums)}
    for i in range(len(nums)):
        rest = target - nums[i]
        if rest in d:
                return [i, d[rest]]


if __name__ == '__main__':
    print(two_sum1([2, 7, 11, 15], 9))








