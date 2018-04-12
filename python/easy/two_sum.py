# Problem:
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


def two_sum1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    >>> two_sum1([2, 7, 11, 15], 9)
    [0, 1]
    """
    for i in range(len(nums)-1):
       for j in range(i+1, len(nums)):
           if nums[i] + nums[j] == target:
               return [i, j]


def two_sum2(nums, target):
    if len(nums) <= 1:
        return False
    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] in buff_dict:
            return [buff_dict[nums[i]], i]
        else:
            buff_dict[target - nums[i]] = i


def two_sum3(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    >>> two_sum1([2, 7, 11, 15], 9)
    [0, 1]
    """
    d = {v: k for k, v in enumerate(nums)}
    for i in range(len(nums)):
        rest = target - nums[i]
        if rest in d:
                return [i, d[rest]]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    from timeit import timeit
    print(timeit('two_sum1([13, 7, 11, 2], 9)', 'from __main__ import two_sum1'))
    print(timeit('two_sum2([13, 7, 11, 2], 9)', 'from __main__ import two_sum2'))
    print(timeit('two_sum3([13, 7, 11, 2], 9)', 'from __main__ import two_sum3'))








