#!/usr/bin/env python
# coding: utf-8
# @Author: lapis-hong
# @Date  : 2018/4/28


def intersection(arr1, arr2):
    """arr1, arr2 is sorted."""
    p1 = 0
    p2 = 0
    n1 = len(arr1)
    n2 = len(arr2)
    res = []
    while p1 < n1 and p2 < n2:
        if arr1[p1] == arr2[p2]:
            res.append(arr1[p1])
            p1 += 1
            p2 += 1
        elif arr1[p1] < arr2[p2]:
            p1 += 1
        else:
            p2 += 1
    return res


if __name__ == '__main__':
    print(intersection([1, 2, 2, 2, 4], [2, 4, 6]))

