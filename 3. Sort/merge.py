# O(n logn)
def merge(arr_a, arr_b):
    i, j = 0, 0
    arr = []
    while i < len(arr_a) and j < len(arr_b):
        if arr_a[i] < arr_b[j]:
            arr.append(arr_a[i])
            i += 1
        elif arr_a[i] > arr_b[j]:
            arr.append(arr_b[j])
            j += 1
    while i < len(arr_a):
        arr.append(arr_a[i])
        i += 1
    while j < len(arr_b):
        arr.append(arr_b[j])
        j += 1
    return arr


def sort(arr):
    if len(arr) == 1:
        return arr
    mid = int(len(arr) / 2)
    left = sort(arr[:mid])
    right = sort(arr[mid:])
    return merge(left, right)


arr = [3, 2, 6, 1, 5, 4]
print(sort(arr))
