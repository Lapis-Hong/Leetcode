# coding: utf-8
__author__ = 'lapis-hong'
__date__ = '2017/8/18'

array = [6, 3, 9, 5, 7, 1, 12, 10, 4, 8, 5]


def quick_sort(L, low, high):
    i = low
    j = high
    if i >= j:
        return L
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:  # from right to left to find the first elem smaller than the key
            j = j-1  # pointer move left
        L[i] = L[j]
        while i < j and L[i] <= key:  # from left to right to find the first elem bigger than the key
            i = i+1  # pointer move right
        L[j] = L[i]
    L[i] = key
    quick_sort(L, low, i-1)
    quick_sort(L, j+1, high)
    return L


def my_quick_sort(arr):  # inplace sort, modify the param
    if len(arr) <= 1:
        return arr
    left = []
    right = []
    base = arr[0]
    for i in arr[1:]:
        if i < base:
            left.append(i)
        else:
            right.append(i)
    left = my_quick_sort(left)
    right = my_quick_sort(right)
    return left + [base] + right


def pythonic_quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    pivots = [i for i in a if i == pivot]
    left = pythonic_quick_sort([i for i in a if i < pivot])  # build a new list
    right = pythonic_quick_sort([i for i in a if i > pivot])
    return left + pivots + right


if __name__ == '__main__':
    #l1 = quick_sort(array, 3, 2)
    l2 = my_quick_sort(array)
    l3 = pythonic_quick_sort(array)
    print(l2)
    print(l3)