from collections import Counter
# coding: utf-8
__author__ = 'lapis-hong'
__date__ = '2017/8/22'

array = [1, 1, 1, 2, 2, 3]
k = 2


def top_k_frequent(array, k):
    return [item[0] for item in Counter(array).most_common(k)]


if __name__ == '__main__':
    print(top_k_frequent(array, k))