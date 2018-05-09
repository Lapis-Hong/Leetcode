# coding: utf-8
"""Prob 347. Top K Frequent Elements

https://leetcode.com/problems/top-k-frequent-elements/description/

Description:
    Given a non-empty array of integers, return the k most frequent elements.
    
    For example,
    Given [1,1,1,2,2,3] and k = 2, return [1,2].
    
    Note: 
    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from collections import Counter


def top_k_frequent(array, k):
    return [item[0] for item in Counter(array).most_common(k)]


if __name__ == '__main__':
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))