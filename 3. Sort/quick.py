def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def pivot(arr, start, end):
    element = arr[start]
    swapIdx = start
    for i in range(start + 1, end + 1):
        if element > arr[i]:
            swapIdx += 1
            swap(arr, swapIdx, i)
    swap(arr, swapIdx, start)
    return swapIdx


def quick(arr, start, end):
    if start < end:
        pivotIdx = pivot(arr, start, end)
        # left
        quick(arr, start, pivotIdx - 1)
        # right
        quick(arr, pivotIdx + 1, end)
    return arr


arr = [4, 8, 2, 1, 5, 7, 6, 3]
# arr = [3, 2, 6, 1, 5, 4]
print(quick(arr, 0, len(arr) - 1))
