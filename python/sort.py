# coding: utf-8
__author__ = 'lapis-hong'
__date__ = '2017/9/21'

arr = [1, 7, 4, 8, 2, 5]


def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        # insert key into arr[0:i-1]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]  # move right
            j = j - 1
        arr[j+1] = key
        # print(arr)
    return arr


def select_sort(arr):
    """time O(n^2), space O(1)"""
    n = len(arr)
    start = 0
    while start < n:
        arr_min = arr[start]
        for i in range(start+1, n):
            if arr[i] < arr[start]:
                arr_min = arr[i]
        arr[start] = arr_min
        start += 1
    return arr


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr


if __name__ == '__main__':
    print(insert_sort(arr))
    print(select_sort(arr))
    print(bubble_sort(arr))
