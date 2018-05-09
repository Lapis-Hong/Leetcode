#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/30
"""Prob 821. Shortest Distance to a Character

https://leetcode.com/problems/shortest-distance-to-a-character/description/

Description:
    Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.
    
    Example 1:
    Input: S = "loveleetcode", C = 'e'
    Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
     
    Note:
    S string length is in [1, 10000].
    C is a single character, and guaranteed to be in string S.
    All letters in S and C are lowercase.
"""


# For each index S[i], let's try to find the distance to the next character C going left,
# and going right. The answer is the minimum of these two values.
def shortestToChar(S, C):
    prev = float('-inf')
    ans = []
    for i, x in enumerate(S):
        if x == C:
            prev = i
        ans.append(i - prev)

    prev = float('inf')
    for i in xrange(len(S) - 1, -1, -1):
        if S[i] == C:
            prev = i
        ans[i] = min(ans[i], prev - i)

    return ans


if __name__ == '__main__':
    print(shortestToChar("loveleetcode", "e"))