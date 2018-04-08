# coding: utf8


def max_subseq_prod(arr):
    """not continuous"""
    max_prod = 1
    max_pos = -100000000000
    for n in arr:
        if n > 1:
            max_prod *= n
        if n < -1:
            max_prod *= n
            if n > max_pos:
                max_pos = n
    if max_prod < 0:
        max_prod /= max_pos
    elif max_prod == 1:  # abs(arr[i]) <= 1
        neg_abs = [abs(n) for n in arr if n < 0]
        if len(neg_abs) >= 2:
            neg_abs.sort()
            max_prod = max(max(arr), neg_abs[-1]*neg_abs[-2])
    return max_prod


def max_substr_prod(arr):
    """continuous"""
    #访问到每个点的时候，以该点为子序列的末尾的乘积，要么是该点本身，要么是该点乘以以前一点为末尾的序列，注意乘积负负得正，故需要记录前面的最大最小值。
    ret, pos_max, neg_max = arr[0], arr[0], arr[0]
    for n in arr:
        pos_max = max(n, max(n*pos_max, n*neg_max))
        neg_max = min(n, min(n*pos_max, n*neg_max))
        ret = max(ret, pos_max)
    return ret

if __name__ == '__main__':
    arr = [0.5, -3, 2, 4, 2, 5] 
    arr = [-0.8, -1, 0.1, 0.3]
    print(max_subseq_prod(arr))
    print(max_substr_prod(arr))
