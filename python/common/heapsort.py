# coding: utf-8
__author__ = 'lapis-hong'
__date__ = '2017/9/2'

arr = [9, 2, 1, 14, 3, 2, 8, 5]


def max_heapify(arr, heap_size, i):
    """parent node: i, left children 2i, right children 2i+1
    O(lgn)"""
    if 2*i <= heap_size:  # has child node
        if 2*i == heap_size:
            largest = 2*i
        else:
            largest = 2*i if arr[2*i-1] >= arr[2*i] else 2*i + 1  # left or right index
        if arr[i-1] < arr[largest-1]:
            arr[i-1], arr[largest-1] = arr[largest-1], arr[i-1]
            max_heapify(arr, heap_size, largest)


def max_heapify2(arr, i):
    """parent node: i, left children 2i, right children 2i+1
    O(lgn)"""
    n = len(arr)
    if 2*i <= n and arr[i-1] < arr[2*i-1]:
        largest = 2*i
    else:
        largest = i
    if (2*i + 1) <= n and arr[largest-1] < arr[2*i]:
        largest = 2*i + 1
    if largest != i:
        arr[i-1], arr[largest-1] = arr[largest-1], arr[i-1]
        max_heapify2(arr, largest)


def build_max_heap(arr):
    """O(n)"""
    heap_size = len(arr)
    for i in range(heap_size//2, 0, -1):
        max_heapify(arr, heap_size, i)


def heap_sort(arr):
    """O(nlgn)"""
    n = len(arr)
    build_max_heap(arr)  # arr[0] is the largest elem
    for i in range(n, 1, -1):  # downto 2
        arr[0], arr[i-1] = arr[i-1], arr[0]
        max_heapify(arr, i-1, 1)
    return arr


print(arr)
# max_heapify2(arr,2)
# build_max_heap(arr)
result = heap_sort(arr)
print(arr)
print(result)
