def binary_search(arr, key):
    """recurrent"""
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (low + high) / 2
        if key < arr[middle]:
            high = middle - 1
        elif key > arr[middle]: 
            low = middle + 1
        else:
            return middle

    return -1


def binary_search2(arr, key):
    """recursive"""
    pass

if __name__ == "__main__":
    arr = [1, 2, 3, 5, 7, 10, 14]
    print(binary_search(arr, 7))
    print(binary_search2(arr, 7))

    

