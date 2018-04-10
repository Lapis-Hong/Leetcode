#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/10
"""Prob 22. Generate Parentheses 

https://leetcode.com/problems/generate-parentheses/description/

Description:
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    
    For example, given n = 3, a solution set is:
    
    [
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"
    ]
"""

# To check whether a sequence is valid, we keep track of balance = opening brackets - closing brackets.
# If it falls below zero at any time, or doesn't end in zero, the sequence is invalid


# If you have two stacks, one for n “(”, the other for n “)”,
# you generate a binary tree from these two stacks of left/right parentheses to form an output string.
# This means that whenever you traverse deeper, you pop one parentheses from one of stacks.
# When two stacks are empty, you form an output string.
def generateParenthesis(n):
    """DFS solution
    :type n: int
    :rtype: List[str]
    """
    res = []

    def dfs(l, r, path, res):
        """
        l: stack of `(`
        r: stack of `)`, remain `)` must more than `(` to be invalid.
        path: 
        """
        if r < l or l == -1 or r == -1:
            return
        if l == 0 and r == 0:
            res.append(path)
        else:
            dfs(l - 1, r, path + "(", res)
            dfs(l, r - 1, path + ")", res)

    dfs(n, n, "", res)
    return (res)


def generateParenthesis2(N):
    """Back Tracking"""
    ans = []

    def backtrack(S='', l=0, r=0):
        if len(S) == 2 * N:
            ans.append(S)
            return
        if l < N:
            backtrack(S + '(', l + 1, r)
        if r < l:
            backtrack(S + ')', l, r + 1)

    backtrack()
    return ans


def generateParenthesis3(N):
    """Closure Number"""
    if N == 0:
        return ['']
    ans = []
    for c in xrange(N):
        for l in generateParenthesis3(c):
            for r in generateParenthesis3(N - 1 - c):
                ans.append('({}){}'.format(l, r))
    return ans


def generateParenthesis4(n, l=0):
    """???"""
    if n > 0 <= l:
        return ['(' + p for p in generateParenthesis4(n-1, l+1)] + [')' + p for p in generateParenthesis4(n, l-1)]
    return [')' * l] * (not n)

if __name__ == '__main__':
    n = 3
    print(generateParenthesis(n))
    print(generateParenthesis2(n))
    print(generateParenthesis3(n))
    print(generateParenthesis4(n))
