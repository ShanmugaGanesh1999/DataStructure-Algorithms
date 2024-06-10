"""
# O(n) - freq ctr
def duplicates(a):
    m = {i: i.count() for i in a}
    for i, j in m.items():
        if j > 1:
            return True
    return False
"""


# O(n) - 2 ptr
def duplicates(a):
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            return True
    return False


# a = [1, 2, 3, 4, 5, 6]  # false
a = [1, 2, 3, 4, 5, 6, 6]  # true
print(duplicates(a))
