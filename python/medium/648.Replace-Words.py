#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/25
"""Prob 648. Replace Words

https://leetcode.com/problems/replace-words/solution/

Description:

    In English, we have a concept called root, which can be followed by some other words to form another longer word - 
    let's call this word successor. For example, the root an, followed by other, which can form another word another.
    Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the 
    sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.
    You need to output the sentence after the replacement.
    
    Example 1:
    Input: dict = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    Output: "the cat was rat by the bat"
    Note:
    The input will only have lower-case letters.
    1 <= dict words number <= 1000
    1 <= sentence words number <= 1000
    1 <= root length <= 100
    1 <= sentence words length <= 1000
"""


def replaceWords(roots, sentence):
    rootset = set(roots)

    def replace(word):
        for i in xrange(1, len(word)):
            if word[:i] in rootset:
                return word[:i]
        return word

    return " ".join(map(replace, sentence.split()))


def replaceWords2(dict, sentence):
    """
    :type dict: List[str]
    :type sentence: str
    :rtype: str
    """
    rootset = set(dict)

    def replace(word):
        res = word
        for root in rootset:
            if word.startswith(root):
                if len(root) < len(res):
                    res = root
        return res

    return " ".join(map(replace, sentence.split()))


def replaceWords3(roots, sentence):
    import collections
    Trie = lambda: collections.defaultdict(Trie)
    trie = Trie()
    END = True

    for root in roots:
        reduce(dict.__getitem__, root, trie)[END] = root

    def replace(word):
        cur = trie
        for letter in word:
            if letter not in cur or END in cur:
                break
            cur = cur[letter]
        return cur.get(END, word)

    return " ".join(map(replace, sentence.split()))


if __name__ == '__main__':
    print(replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery"))