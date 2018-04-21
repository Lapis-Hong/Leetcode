#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/17
"""Prob 783. Minimum Distance Between BST Nodes

https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/

Description:
    Given a Binary Search Tree (BST) with the root node root, 
    return the minimum difference between the values of any two different nodes in the tree.
    
    Example :
    
    Input: root = [4,2,6,1,3,null,null]
    Output: 1
    Explanation:
    Note that root is a TreeNode object, not an array.
    
    The given tree [4,2,6,1,3,null,null] is represented by the following diagram:
    
              4
            /   \
          2      6
         / \    
        1   3  
    
    while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
    Note:
    
    The size of the BST will be between 2 and 100.
    The BST is always valid, each node's value is an integer, and each node's value is different.
"""


def minDiffInBST(root):
    """Recursive way using inorder traverse
    :type root: TreeNode
    :rtype: int
    """
    def inorder(root, res):
        if root is None:
            return res
        inorder(root.left, res)
        res.append(root.val)
        inorder(root.right, res)
        return res

    inorder_list = inorder(root, [])
    return min([inorder_list[i+1] - inorder_list[i] for i in range(len(inorder_list)-1)])


def minDiffInBST2(root):
    """Iterative, find all the element, sort, then find min diff.
    :type root: TreeNode
    :rtype: int
    """
    nodes = []
    q = [root]
    while q:
        root = q.pop()
        nodes.append(root.val)
        if root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)
    nodes.sort()

    return min([nodes[i+1] - nodes[i] for i in range(len(nodes)-1)])