#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/24
"""Prob 459. Repeated Substring Pattern

https://leetcode.com/problems/repeated-substring-pattern/description/

Description:

    Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
    Example 1:
    Input: "abab"
    Output: True
    Explanation: It's the substring "ab" twice.
    
    Example 2:
    Input: "aba"
    Output: False
    
    Example 3:
    Input: "abcabcabcabc" 
    Output: True
    Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""


# For example, substring repeat 4 times, so we name each part as A,B,C,D. And our goal is to prove: A = B = C = D.
# Repeating S twice, and then destroying first and last parts.
# If you can find S in Any Position , you can always get A = B = C = D
def repeatedSubstringPattern(str):
    """First char of input string is first char of repeated substring
        Last char of input string is last char of repeated substring
        Let S1 = S + S (where S in input string)
        Remove 1 and last char of S1. Let this be S2
        If S exists in S2 then return true else false
        Let i be index in S2 where S starts then repeated substring length i + 1 and repeated substring S[0: i+1]
    """
    return str in (2 * str)[1:-1]


def repeatedSubstringPattern1(s):
    """
    :type s: str
    :rtype: bool
    """
    n = len(s)
    for i in range(1, n / 2 + 1):
        pattern = s[:i]
        if n % i == 0:
            # if pattern*(len(s)/i) == s:
            match = 0
            for j in range(n / i):
                if pattern != s[j * i:(j + 1) * i]:
                    break
                else:
                    match += 1
            if match == n / i:
                return True
    return False


def repeatedSubstringPattern2(s):
    """
    :type s: str
    :rtype: bool
    """
    n = len(s)
    for i in range(1, n / 2 + 1):
        pattern = s[:i]
        if n % i == 0:
            if pattern*(len(s)/i) == s:
                return True
    return False



if __name__ == '__main__':
    print(repeatedSubstringPattern('aba'))