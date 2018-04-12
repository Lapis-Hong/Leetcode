#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lapis-hong
# @Date  : 2018/2/20
"""Prob 151. Reverse Words in a String

https://leetcode.com/problems/reverse-words-in-a-string/description/

Description:
    Given an input string, reverse the string word by word.
    
    For example,
    Given s = "the sky is blue",
    return "blue is sky the".
    
    Clarification:
    What constitutes a word?
    A sequence of non-space characters constitutes a word.
    Could the input string contain leading or trailing spaces?
    Yes. However, your reversed string should not contain leading or trailing spaces.
    How about multiple spaces between two words?
    Reduce them to a single space in the reversed string.
"""


def reverse_words(s):
    """Refer solution
    """
    return " ".join(s.split()[::-1])  # ' '.join(reversed(s.split()))
    # If sep is not specified or is None, any
    # whitespace string is a separator and empty strings are removed
    # from the result.


if __name__ == '__main__':
    print(reverse_words("the sky is blue"))
