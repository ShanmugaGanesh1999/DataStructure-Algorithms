def compare_strings(x, y) -> int:
    if x < y:
        return -1
    elif x > y:
        return 1
    return 0


def binary_search(arr, x) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def find_missing_string(D, C) -> str:
    for i in C:
        index = binary_search(D, i)
        D[index] = 0
    for i in D:
        if i != 0:
            return i


D = ["coffee", "kombucha", "slushy", "soda", "tea"]
C = ["kombucha", "tea", "soda", "coffee"]
missing_string = find_missing_string(D, C)
print(missing_string)
