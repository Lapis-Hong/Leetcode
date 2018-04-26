#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/26
"""Prob 49. Group Anagrams

https://leetcode.com/problems/group-anagrams/description/

Description:

Given an array of strings, group anagrams together.

    Example:
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
    Output:
    [
      ["ate","eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]
    Note:
    All inputs will be in lowercase.
    The order of your output does not matter.
"""


def groupAnagrams(strs):
    """Two strings are anagrams if and only if their sorted strings are equal.
    """
    import collections
    ans = collections.defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return ans.values()


def groupAnagrams2(strs):
    """Two strings are anagrams if and only if their character counts 
    (respective number of occurrences of each character) are the same.
    """
    import collections
    ans = collections.defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
    return ans.values()

