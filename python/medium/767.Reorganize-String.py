#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/10
"""Prob 767. Reorganize String
Description:
    Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
    
    If possible, output any possible result.  If not possible, return the empty string.
    
    Example 1:
    
    Input: S = "aab"
    Output: "aba"
    Example 2:
    
    Input: S = "aaab"
    Output: ""
    Note:
    
    S will consist of lowercase letters and have length in range [1, 500].
"""
import heapq


# Approach #1: Sort by Count
def reorganize_string(s):
    """
    :type s: str
    :rtype: str
    """
    n = len(s)
    a = []
    # letter count
    for c, x in sorted((s.count(x), x) for x in set(s)):
        if c > (n + 1) / 2:
            return ""
        a.extend(c * x)
    ans = [None] * n
    #
    ans[::2], ans[1::2] = a[n / 2:], a[:n / 2]
    return "".join(ans)


# Approach #2: Greedy with Heap
# Intuition
# A greedy approach that tries to write the most common letter (that isn't the same as the previous letter) will work.
# The reason is that the task is only impossible if the frequency of a letter exceeds (N+1) / 2.
# Writing the most common letter followed by the second most common letter keeps this invariant.
# A heap is a natural structure to repeatedly return the current top 2 letters with the largest remaining counts.
# Approach
# We store a heap of (count, letter). [In Python, our implementation stores negative counts.]
# We pop the top two elements from the heap (representing different letters with positive remaining count),
# then write the most frequent one that isn't the same as the most recent one. Push correct counts back onto the heap.
# Actually, we don't even need to keep track of the most recent one written. If it is possible to organize the string,
# the letter written second can never be written first in the very next writing.
# At the end, we might have one element still on the heap, which must have a count of one.
# If we do, we'll add that to the answer too.
def reorganize_string2(s):
    pq = [(-s.count(x), x) for x in set(s)]
    # Transform list into a heap, in-place, in O(len(heap)) time.
    heapq.heapify(pq)
    if any(-nc > (len(s) + 1) / 2 for nc, x in pq):
        return ""

    ans = []
    while len(pq) >= 2:
        nct1, ch1 = heapq.heappop(pq)
        nct2, ch2 = heapq.heappop(pq)
        # This code turns out to be superfluous, but explains what is happening
        # if not ans or ch1 != ans[-1]:
        #    ans.extend([ch1, ch2])
        # else:
        #    ans.extend([ch2, ch1])
        ans.extend([ch1, ch2])
        if nct1 + 1:
            heapq.heappush(pq, (nct1 + 1, ch1))
        if nct2 + 1:
            heapq.heappush(pq, (nct2 + 1, ch2))

    return "".join(ans) + (pq[0][1] if pq else '')


def reorganize_string3(s):
    a = sorted(sorted(s), key=s.count)
    h = len(a) / 2
    # put the most common letters at the even indexes
    a[1::2], a[::2] = a[:h], a[h:]
    return ''.join(a) * (a[-1] != a[-2:-1])  # a[-1:] a[-1] last element

if __name__ == '__main__':
    print(reorganize_string('aaabbc'))
    print(reorganize_string2('aaabbc'))
