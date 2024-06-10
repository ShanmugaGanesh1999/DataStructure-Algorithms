# O(log n) - 2 ptr
def sortedSumZero(a):
    i, j = 0, len(a) - 1  # left,right
    while i < j:
        k = a[i] + a[j]  # sum
        if k == 0:
            return [a[i], a[j]]
        elif k > 0:
            j -= 1
        else:
            i += 1
    return None


"""
# O(n^2)
def sortedSumZero(a):
    for i in range(0, len(a)):
        for j in range(i, len(a)):
            if a[i] + a[j] == 0:
                return [a[i], a[j]]
    return None
"""


# a = [-3, -1, 0, 2, 3]  # [-3,3]
# a = [-2, 0, 2, 3]  # [-2,2]
a = [-1, 0, 2, 3]  # None
print(sortedSumZero(a))
