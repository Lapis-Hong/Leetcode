# Problem:
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Examples:
# nums1 = [1, 2]
# nums2 = [3, 4]
# The median is (2 + 3)/2 = 2.5
def median(nums):
    """
    find the median of a sorted array
    :param nums: Dict{} like {0:v1,1:v2,...} or List[int]
    :return: float
    """
    k = len(nums)
    assert k >= 1
    if k % 2 == 1:
        return nums[(k-1)/2]
    else:
        return (nums[(k-2)/2] + nums[k/2])/float(2)


def findMedianSortedArrays1(nums1, nums2):
    """
    merge into one list, but O(m+n)
    """
    d1 = nums1
    d2 = nums2
    all = []
    while len(d1) & len(d2):
        for num1 in d1:
            for num2 in d2:
                if num1 >= num2:
                    num2_index = d2.index(num2)
                    all.append(d2.pop(num2_index))
                else:
                    num1_index = d1.index(num1)
                    all.append(d1.pop(num1_index))
                    break
    if len(d1) > 0:
        all.extend(d1)
    if len(d2) > 0:
        all.extend(d2)
    return median(all)


def findMedianSortedArrays2(nums1, nums2):
    """remove one element a time both from head and tail to find the median"""
    from collections import deque
    deque1 = deque(nums1)
    deque2 = deque(nums2)
    while len(deque1) & len(deque2):
        if deque1[0] <= deque2[0]:
            deque1.popleft()
        else: deque2.popleft()
        if deque1[len(deque1)-1] >= deque2[len(deque2)-1]:
            deque1.pop()
        else: deque2.pop()
    if len(deque1) > 0:
        return deque1, median(deque1)
    else: return deque2,median(deque2)


def findMedianSortedArrays3(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    from math import floor
    while len(nums1) & len(nums2):
        if len(nums1) < len(nums2):
            rm_index = floor(len(nums1)/2)
            nums1 = nums1[rm_index:]
            nums2 = nums2[:len(nums2)-rm_index]
    if len(nums1) > 0:
        return median(nums1)
    else:
        return median(nums2)



if __name__ == '__main__':
    import time
    nums1 = [1, 2]
    nums2 = [3, 4]
    
    t0 = time.time()
    print(findMedianSortedArrays1(nums1, nums2))
    t1 = time.time()

    print(t1 - t0)
    t0 = time.time()
    print(findMedianSortedArrays2(nums1, nums2))
    t1 = time.time()

    print(t1-t0)
    t0 = time.time()
    print(findMedianSortedArrays3(nums1, nums2))
    t1 = time.time()
    print(t1 - t0)











