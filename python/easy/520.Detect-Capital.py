#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/21
"""Prob 520. Detect Capital

https://leetcode.com/problems/detect-capital/description/

Description:
    Given a word, you need to judge whether the usage of capitals in it is right or not.
    
    We define the usage of capitals in a word to be right when one of the following cases holds:
    
    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital if it has more than one letter, like "Google".
    Otherwise, we define that this word doesn't use capitals in a right way.
    Example 1:
    Input: "USA"
    Output: True
    Example 2:
    Input: "FlaG"
    Output: False
    Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""


def detectCapitalUse1(word):
    """
    :type word: str
    :rtype: bool
    """
    return word[1:] == word[1:].lower() or word==word.upper()


def detectCapitalUse2(word):
    return word.isupper() or word.islower() or word.istitle()


if __name__ == '__main__':
    print(detectCapitalUse1('FlaG'))
    print(detectCapitalUse2('FlaG'))

