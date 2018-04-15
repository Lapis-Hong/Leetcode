#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/15
"""Prob 139. Word Break

https://leetcode.com/problems/word-break/description/

Description:
    Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
    determine if s can be segmented into a space-separated sequence of one or more dictionary words. 
    You may assume the dictionary does not contain duplicate words.
    
    For example, given
    s = "leetcode",
    dict = ["leet", "code"].
    
    Return true because "leetcode" can be segmented as "leet code".
    
    UPDATE (2017/1/4):
    The wordDict parameter had been changed to a list of strings (instead of a set of strings). 
    Please reload the code definition to get the latest changes.
"""


def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    word_set = set(wordDict)
    if s in wordDict:
        return True
    for i in range(len(s)):
        s1 = s[:i]
        s2 = s[i:]
        if s1 in word_set:
            if wordBreak(s2, wordDict):
                return True

    return False


def wordBreak2(s, words):
    """DP"""
    dp = [True]
    for i in range(1, len(s)+1):
        dp += any(dp[j] and s[j:i] in words for j in range(i)),
    return dp[-1]


def wordBreak3(s, wordDict):
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: bool
    """
    # dp[i] means s[:i+1] can be segmented into words in the wordDicts
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(len(s)):
        for j in range(i, len(s)):
            if dp[i] and s[i: j + 1] in wordDict:
                dp[j + 1] = True

    return dp


if __name__ == '__main__':
    print(wordBreak('leetcode', ['leet', 'code']))
    # TLE
    print(wordBreak2(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
        ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
    print(wordBreak3("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
        ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
