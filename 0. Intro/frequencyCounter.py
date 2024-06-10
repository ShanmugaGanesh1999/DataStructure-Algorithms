# O(n) - freq counter
def freqCtr(a, b):
    if len(a) != len(b):
        return False
    m = {i: a.count(i) for i in a}
    n = {i: b.count(i) for i in b}
    for i, j in m.items():
        if (i**2 not in n) or (n[i**2] != j):
            return False
    return True


"""
#O(n^2)
def freqCtr(a, b):
    if len(a) != len(b):
        return False
    for i in range(len(b)):
        is_present = False
        for j in range(len(a)):
            if a[j] > 0 and b[i] > 0 and a[j]**2 == b[i]:
                is_present = True
                a[j] = -1
                b[i] = -1
                break
        if not is_present:
            return False
    return True
"""

# a = [1, 2, 3]
# b = [1, 4, 9]  # true
a = [1, 2, 1]
b = [4, 4, 1]  # false
print(freqCtr(a, b))
