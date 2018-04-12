#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: lapis-hong
# @Date  : 2018/4/10
"""Prob 93. Restore IP Addresses

Description:
    Given a string containing only digits, restore it by returning all possible valid IP address combinations.
    For example:
    Given "25525511135",
    return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""


def restore_ip_addresses(s):
    """
    :type s: str
    :rtype: List[str]
    """

    def is_ip(s):
        """ips start from 0 to 255"""
        if len(s) == 1:
            return True
        elif len(s) == 2 and s[0] != 0:
            return True
        elif len(s) == 3:
            return 100 <= int(s) <= 255
        else:
            return False

    def is_ip_2(s):
        ip_list = []
        if len(s) < 2 or len(s) > 6:
            return []
        else:
            for i in range(3):
                head = s[:i+1]
                tail = s[i+1:]
                if is_ip(head) and is_ip(tail):
                    ip_list.append(head + '.' + tail)
            return ip_list

    def is_ip_3(s):
        ip_list = []
        if len(s) < 3 or len(s) > 9:
            return []
        else:
            for i in range(3):
                head = s[:i+1]
                tail = s[i+1:]
                if is_ip(head) and is_ip_2(tail):
                    ip_list.extend([head + '.' + ip for ip in is_ip_2(tail)])
            return ip_list

    ret = []
    if len(s) < 4 or len(s) > 12:
        return []
    else:
        for i in range(3):
            head = s[:i+1]
            tail = s[i+1:]
            if is_ip(head) and is_ip_3(tail):
                ret.extend([head + '.' + ip for ip in is_ip_3(tail)])
    return ret


def restore_ip_addresses2(s):
    """using DFS to find all possibilities"""
    def dfs(s, index, path, res):
        if index == 4:
            if not s:
                res.append(path[:-1])
            return  # backtracking
        for i in xrange(1, 4):
            # the digits we choose should no more than the length of s
            if i <= len(s):
                # choose one digit
                if i == 1:
                    dfs(s[i:], index + 1, path + s[:i] + ".", res)
                # choose two digits, the first one should not be "0"
                elif i == 2 and s[0] != "0":
                    dfs(s[i:], index + 1, path + s[:i] + ".", res)
                # choose three digits, the first one should not be "0", and should less than 256
                elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                    dfs(s[i:], index + 1, path + s[:i] + ".", res)

    res = []
    dfs(s, 0, "", res)
    return res

if __name__ == '__main__':
    print(restore_ip_addresses('25525511135'))
    print(restore_ip_addresses2('25525511135'))
    print(restore_ip_addresses('0002'))