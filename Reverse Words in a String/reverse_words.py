#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lapis-hong
# @Date  : 2018/2/20
"""
https://leetcode.com/problems/reverse-words-in-a-string/description/

Problem 151. Reverse Words in a String

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
    """My solution
    Args: string
    Return: reversed string
    """
    result = []
    words = s.strip().split(' ')
    words = [w for w in words if w]
    for i in range(len(words)):
        result.append(words.pop())
    return ' '.join(result)


def reverse_words_2(s):
    """Refer solution
    """
    return " ".join(s.split()[::-1])
    # If sep is not specified or is None, any
    # whitespace string is a separator and empty strings are removed
    # from the result.
    # or return ' '.join(reversed(s.split()))


if __name__ == '__main__':
    test_string = ' I love  you'
    print(reverse_words(test_string))
    print(reverse_words_2(test_string))
