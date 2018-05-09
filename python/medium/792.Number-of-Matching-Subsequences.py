#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/5/1
"""Prob 792. Number of Matching Subsequences

https://leetcode.com/problems/number-of-matching-subsequences/description/

Description:
    Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.
    
    Example :
    Input: 
    S = "abcde"
    words = ["a", "bb", "acd", "ace"]
    Output: 3
    Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
    Note:
    All words in words and S will only consists of lowercase letters.
    The length of S will be in the range of [1, 50000].
    The length of words will be in the range of [1, 5000].
    The length of words[i] will be in the range of [1, 50].
"""


def numMatchingSubseq(S, words):
    """Using 2 pointers. O(m*n)
    :type S: str
    :type words: List[str]
    :rtype: int
    """
    res = 0
    n1 = len(S)
    for w in words:
        n2 = len(w)
        pt1 = 0
        pt2 = 0
        while pt1 < n1 and n1 - pt1 >= n2 - pt2:
            if pt2 == n2 - 1 and S[pt1] == w[pt2]:
                res += 1
                break
            elif S[pt1] == w[pt2]:
                pt2 += 1
                pt1 += 1
            else:
                pt1 += 1
    return res


def numMatchingSubseq2(S, words):
    """
    :type S: str
    :type words: List[str]
    :rtype: int
    """
    num = 0
    for i in words:
        index = 0
        flag = 0
        for j in i:
            index = S.find(j, index)  # find return -1, but index raise ValueError when the substring is not found.
            if index == -1:
                flag = 1
                break
            index += 1
        if flag == 0:
            num += 1
    return num


if __name__ == '__main__':
    print(numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))