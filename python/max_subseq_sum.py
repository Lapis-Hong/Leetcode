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
    cur_sum, max_sum = arr[0], arr[0]
    for n in arr[1:]:
        cur_sum += n
        if cur_sum > max_sum:
            max_sum = cur_sum
        elif cur_sum < 0:
            cur_sum = 0
    return max_sum


def max_substr_sum2(arr):
    """continuous"""
    # dynamic programming: sum[i] = MAX{sum[i-1] + a[i], a[i]}
    max_sum = arr[0]
    for n in arr[1:]:
        max_sum += n
        max_sum = max(max_sum, n)
    if max_sum < arr[0]:
        max_sum = arr[0]
    return max_sum


if __name__ == '__main__':
    arr = [12, -13, 4, 8, -2, 5]
    arr = [-3, -5, -8, -10]
    print(max_subseq_sum(arr))
    print(max_substr_sum(arr))
    print(max_substr_sum2(arr))

