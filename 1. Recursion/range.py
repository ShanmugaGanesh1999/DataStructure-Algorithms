# O(n)
def rangeOf(n):
    if n == 0:
        return 0
    return n + rangeOf(n - 1)


n = 5
print(rangeOf(n))
