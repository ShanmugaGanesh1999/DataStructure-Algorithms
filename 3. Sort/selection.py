def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


# O(n) - smallest number sorted at first, then second smallest ...
def selection(arr):
    for i in range(0, len(arr)):
        small = i
        for j in range(i + 1, len(arr)):
            if arr[small] > arr[j]:
                small = j
        if small != i:
            swap(arr, small, i)
    return arr


# arr = [9, 1, 2, 3, 4, 5, 6, 7, 8]
arr = [2, 8, 4, 9, 3, 5, 6, 1, 7]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(selection(arr))
