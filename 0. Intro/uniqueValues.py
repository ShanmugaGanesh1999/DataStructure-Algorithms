"""
# O(n)
def sortedUniqueValues(a):
    return len(set(a))
"""


# O(n) - 2 ptr
def sortedUniqueValues(a):
    if not len(a):
        return 0
    i = 0
    for j in range(len(a)):
        if a[i] != a[j]:
            i += 1
            a[i] = a[j]
    return i + 1


# a = [1, 1, 1, 1, 1, 3]  # 2
# a = []  # 0
a = [-2, -1, -1, -1, 0, 1]  # 4
print(sortedUniqueValues(a))
