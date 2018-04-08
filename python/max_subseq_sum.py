def max_subseq_sum(arr):
    """not continuous"""
    max_sum = 0
    for n in arr:
        if n > 0:
            max_sum += n
    if max_sum == 0:
        max_sum = max(arr)
    return max_sum


def max_substr_sum(arr):
    """continuous"""
    cur_sum, max_sum = 0, -10000000000
    for n in arr:
        cur_sum += n
        if cur_sum > max_sum:
            max_sum = cur_sum
        elif cur_sum < 0:
            cur_sum = 0
    return max_sum


if __name__ == '__main__':
    arr = [12, -13, 4, 8, -2, 5]
#    arr = [-3, -5, -8, -10]
    print(max_subseq_sum(arr))
    print(max_substr_sum(arr))


