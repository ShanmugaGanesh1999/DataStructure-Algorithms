# O(n) - smallest number sorted at first, then second smallest ...
def insertion(arr):
    for i in range(1, len(arr)):
        cur_val = arr[i]
        j = i - 1
        while j >= 0 and cur_val < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = cur_val
    return arr


# arr = [9, 1, 2, 3, 4, 5, 6, 7, 8]
arr = [2, 8, 4, 9, 3, 5, 6, 1, 7]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(insertion(arr))
