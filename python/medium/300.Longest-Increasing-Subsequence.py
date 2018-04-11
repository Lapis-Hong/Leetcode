#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/11
"""Prob 300. Longest Increasing Subsequence (LSI)

https://leetcode.com/problems/longest-increasing-subsequence/description/

Description:
    Given an unsorted array of integers, find the length of longest increasing subsequence.
    
    For example,
    Given [10, 9, 2, 5, 3, 7, 101, 18],
    The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.
    
    Your algorithm should run in O(n2) complexity.
    
    Follow up: Could you improve it to O(n log n) time complexity?
"""


def lengthOfLIS(nums):
    """O(nlogn)"""
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) / 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size


# dp[i] represents the length of the longest increasing subsequence at index i
def lengthOfLIS2(nums):
    """DP O(n^2)
     dp[1] = 1; dp[i] = max{1,dp[j]+1 | a[j]<a[i] and j<i} or max{dp[j]}+1
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    dp = [1]*len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

# d = [1]*len(lis)
# res = 1
# for i in range(len(lis)):
#     for j in range(i):
#         if lis[j] <= lis[i] and d[i] < d[j]+1:
#             d[i] = d[j]+1
#         if d[j] >  res:
#             res = d[j]
# print res


# 当dp[i]一样时，尽量选择更小的a[x].
# 原序列为1，5，8，3，6，7
# 栈为1，5，8，此时读到3，用3替换5，得到1，3，8； 再读6，用6替换8，得到1，3，6；再读7，得到最终栈为1，3，6，7。最长递增子序列为长度4。
def lengthOfLIS3(nums):
    """Binary Search. O(nlogn)"""
    def search(temp, l, r, target):
        """binary search"""
        if l == r:
            return l
        mid = (l+r)/2
        return search(temp, mid+1, r, target) if temp[mid] < target else search(temp, l, mid, target)

    temp = []
    for num in nums:
        pos = search(temp, 0, len(temp), num)
        if pos >= len(temp):
            temp.append(num)
        else:
            temp[pos] = num
    return len(temp)

if __name__ == '__main__':
    print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(lengthOfLIS2([10, 9, 2, 5, 3, 7, 101, 18]))
    print(lengthOfLIS3([10, 9, 2, 5, 3, 7, 101, 18]))