#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/27
"""Prob 404. Sum of Left Leaves

https://leetcode.com/problems/sum-of-left-leaves/description/

Description:

    Find the sum of all left leaves in a given binary tree.
    
    Example:
    
        3
       / \
      9  20
        /  \
       15   7
    
    There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""


def sumOfLeftLeaves(root):
    """Recursive
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    res = 0
    if root.left:
        if not root.left.left and not root.left.right:  # left leaf
            res += root.left.val
        else:
            res += sumOfLeftLeaves(root.left)
    if root.right:
        res += sumOfLeftLeaves(root.right)
    return res


def sumOfLeftLeaves2(root):
    """Iterative using stack
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    stack = [root]
    res = 0
    while stack:
        node = stack.pop(0)
        if node.left:
            if not node.left.left and not node.left.right:
                res += node.left.val
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res


