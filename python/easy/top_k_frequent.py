# coding: utf-8
from collections import Counter


def top_k_frequent(array, k):
    return [item[0] for item in Counter(array).most_common(k)]


if __name__ == '__main__':
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))