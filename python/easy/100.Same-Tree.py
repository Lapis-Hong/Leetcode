#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/5/9
"""Prob 100. Same Tree

https://leetcode.com/problems/same-tree/description/

Description:
    Given two binary trees, write a function to check if they are the same or not. 
    Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
    
    Example 1:
    Input:     1         1
              / \       / \
             2   3     2   3
    
            [1,2,3],   [1,2,3]
    
    Output: true
    Example 2:
    Input:     1         1
              /           \
             2             2
    
            [1,2],     [1,null,2]
    
    Output: false
    Example 3:
    Input:     1         1
              / \       / \
             2   1     1   2
    
            [1,2,1],   [1,1,2]
    
    Output: false
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if not p and not q:
        return True
    elif (not p and q) or (not q and p):
        return False
    else:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


def isSameTree2(p, q):
    stk = [(p, q)]
    while stk:
        x, y = stk.pop()
        if not x or not y:
            if x is y:
                continue
            return False
        if x.val != y.val:
            return False
        stk.extend([(x.left, y.left), (x.right, y.right)])
    return True

