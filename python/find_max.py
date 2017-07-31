import time
from python.clock import clock
# two sorted list, the max of second list < the min of first list, find the max element
a = [100, 101, 102, 104, 200, 400, 500, 1, 2, 3, 4, 5]
b = range(10000, 20000, 1) + range(1000)
c = [2, 3, 4, 1]


@clock
def find_max(array):  # better method, faster and stable
    head = 0
    tail = len(array)
    mid = int(0.5*tail)  # do not need to care about 2k or 2k+1
    while head < tail:
        if array[mid-1] < array[mid] and array[mid] > array[mid+1]:  # maximum condition
            return array[mid]
        else:
            if array[mid] < array[-1]:
                tail = mid
                mid = int(0.5*tail)
            else:
                head = mid
                mid = head + int(0.5*(tail-head))


def find_max2(array):  # Warning: array[-1] may change when call the find_max2, not work
    if len(array) < 3:
        return array[1] if array[0] < array[1] else array[0]
    mid = int(0.5*len(array))
    if array[mid - 1] < array[mid] and array[mid] > array[mid + 1]:
        return array[mid]
    else:
        if array[mid] < array[-1]:
            print(array[:mid])
            return find_max2(array[:mid])

        else:
            print(array[mid:])
            return find_max2(array[mid:])


result11 = find_max(a)
result12 = find_max(b)
result13 = find_max(c)
result21 = find_max2(a)
t0 = time.time()
result22 = find_max2(b)
result23 = find_max2(c)
print(find_max2.__name__ + '() Take {} sec.'.format(time.time()-t0))
print(result11, result12, result13)
print(result21, result22, result23)





