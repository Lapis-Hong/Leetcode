#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/28
"""Prob 20. Valid Parentheses

https://leetcode.com/problems/valid-parentheses/description/

Description:
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.
    
    Example 1:
    Input: "()"
    Output: true
    
    Example 2:
    Input: "()[]{}"
    Output: true
    
    Example 3:
    Input: "(]"
    Output: false
    
    Example 4:
    Input: "([)]"
    Output: false
    
    Example 5:
    Input: "{[]}"
    Output: true
"""


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    for c in s:
        if c in {"{", "(", "["}:
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            curr_bracket = stack[-1] + c
            if curr_bracket not in {"{}", "[]", "()"}:
                return False
            stack.pop()
    return len(stack) == 0  # not stack


if __name__ == '__main__':
    print(isValid("([)]"))