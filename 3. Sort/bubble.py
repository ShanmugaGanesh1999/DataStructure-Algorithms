def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


# O(n^2) - largest number sorted at first, then second largest ..,
def bubble(arr):
    for i in range(len(arr)):
        no_swaps = True
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
                no_swaps = False
        if no_swaps:
            break
    return arr


arr = [9, 1, 2, 3, 4, 5, 6, 7, 8]
# arr = [2, 8, 4, 9, 3, 5, 6, 1, 7]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(bubble(arr))
