# O(n) - smallest number sorted at first, then second smallest ...
def insertion(arr):
    for i in range(1, len(arr)):
        j = i
        k = arr[i]
        while j > 0 and arr[j - 1] > k:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = k
    return arr


# arr = [9, 1, 2, 3, 4, 5, 6, 7, 8]
arr = [2, 8, 4, 9, 3, 5, 6, 1, 7]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(insertion(arr))
