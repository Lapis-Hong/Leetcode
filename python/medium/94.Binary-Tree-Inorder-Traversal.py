#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/15
""" Prob 94. Binary Tree Inorder Traversal (LDR)

https://leetcode.com/problems/binary-tree-inorder-traversal/description/

Description:
    Given a binary tree, return the inorder traversal of its nodes' values.
    
    For example:
    Given binary tree [1,null,2,3],
       1
        \
         2
        /
       3
    return [1,3,2].
    
    Note: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def inorderTraversal1(root):
    """Recursive Approach
    Time complexity: O(n)
    Space complexity: O(log(n))
    """
    def helper(root, res):
        if root:
            helper(root.left, res)
            res.append(root.val)
            helper(root.right, res)
    res = []
    helper(root, res)
    return res


def inorderTraversal(root):
    """Iteratively Approach Using Stack
    Time complexity: O(n)
    Space complexity: O(n)
    """
    res, stack = [], []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        node = stack.pop()
        res.append(node.val)
        root = node.right
    return res


