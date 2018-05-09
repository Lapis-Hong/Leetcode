#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/5/3
"""Prob 3. Longest Substring Without Repeating Characters

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Description:
    Given a string, find the length of the longest substring without repeating characters.
    
    Examples:
    Given "abcabcbb", the answer is "abc", which the length is 3.
    Given "bbbbb", the answer is "b", with the length of 1.
    Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, 
    "pwke" is a subsequence and not a substring.
"""


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    res = 0
    start = 0
    end = 0
    for c in s:
        if c not in s[start:end]:
            end += 1
        else:
            if len(s[start:end]) > res:
                res = len(s[start:end])
            start += s[start:end].find(c) + 1
            end += 1
    return max(res, len(s[start:end]))


def lengthOfLongestSubstring2(s):
    longest = []
    max_length = 0

    for c in s:
        if c in longest:
            max_length = max(max_length, len(longest))
            longest = longest[longest.index(c) + 1:]
        longest.append(c)
    return max(max_length, len(longest))

if __name__ == '__main__':
    print(lengthOfLongestSubstring("pwwkew"))
