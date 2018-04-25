#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/25
"""Prob 692. Top K Frequent Words

https://leetcode.com/problems/top-k-frequent-words/description/

Description:
    Given a non-empty list of words, return the k most frequent elements. 
    Your answer should be sorted by frequency from highest to lowest. 
    If two words have the same frequency, then the word with the lower alphabetical order comes first.
    
    Example 1:
    Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
    Output: ["i", "love"]
    Explanation: "i" and "love" are the two most frequent words.
        Note that "i" comes before "love" due to a lower alphabetical order.
    Example 2:
    Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
    Output: ["the", "is", "sunny", "day"]
    Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
        with the number of occurrence being 4, 3, 2 and 1 respectively.
    Note:
    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Input words contain only lowercase letters.
    Follow up:
    Try to solve it in O(n log k) time and O(n) extra space.
"""


def topKFrequent(words, k):
    """
    :type words: List[str]
    :type k: int
    :rtype: List[str]
    """
    d = {}
    for w in words:
        d[w] = d.get(w, 0) + 1

    d = sorted(d.items(), key=lambda d: (-d[1], d[0]))
    return [w[0] for w in d[:k]]
    # ret = sorted(d, key=lambda w: (-d[w], w))
    # return ret[:k]


def topKFrequent2(words, k):
    import collections
    count = collections.Counter(words)
    candidates = count.keys()
    candidates.sort(key = lambda w: (-count[w], w))
    return candidates[:k]

if __name__ == '__main__':
    print(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
    print(topKFrequent(["aaa", "aa", "a"], 1))