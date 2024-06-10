# O(log n) - divide & conquer
def search(a, n):
    if not len(a):
        return -1
    l, r = 0, len(a) - 1
    while l < r:
        m = int((l + r) / 2)
        if a[m] == n:
            return m
        elif a[m] > n:
            r = m - 1
        else:
            l = m + 1
    return -1


"""
# O(n)
def search(a, n):
    for idx, i in enumerate(a):
        if n == i:
            return idx
    return -1
"""

# a, n = [1, 2, 3, 4, 5, 6], 4  # 3
a, n = [1, 2, 3, 4, 5, 6], 7  # -1
print(search(a, n))
