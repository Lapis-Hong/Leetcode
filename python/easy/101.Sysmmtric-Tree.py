#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/16
"""Prob 101. Symmetric Tree

https://leetcode.com/problems/symmetric-tree/description/

Description:
    Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
    For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    But the following [1,2,2,null,3,null,3] is not:
        1
       / \
      2   2
       \   \
       3    3
    Note:
    Bonus points if you could solve it both recursively and iteratively.
"""


def isSymmetric(root):
    """Recursive
    :type root: TreeNode
    :rtype: bool
    """
    def isMirror(t1, t2):
        if not t1 and not t2:  # both empty
            return True
        elif not t1 or not t2:  # only one node is empty
            return False
        return t1.val == t2.val and isMirror(t1.left == t2.right) and isMirror(t1.right == t2.left)

    return isMirror(root, root)


def isSymmetric2(root):
    """Iterative using queue or stack
    :type root: TreeNode
    :rtype: bool
    """
    q = [root, root]
    while q:
        node1 = q.pop()
        node2 = q.pop()
        if not node1 and not node2:
            continue
        elif not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        q.extend([node1.left, node2.right, node1.right, node2.left])
    return True



