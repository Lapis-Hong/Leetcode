#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/10
"""Prob 557. Reverse Words in a String III

https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

Description:
    Given a string, you need to reverse the order of characters in each word within a sentence 
    while still preserving whitespace and initial word order.

    Example 1:
    Input: "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"
    Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""


def reverse_words(s):
    """
    :type s: str
    :rtype: str
    """
    return ' '.join([w[::-1] for w in s.split(' ')])


if __name__ == '__main__':
    print(reverse_words("Let's take LeetCode contest"))