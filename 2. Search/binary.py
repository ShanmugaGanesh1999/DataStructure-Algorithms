def binary(a, n, l, r):
    if l > r:
        return -1
    m = int((l + r) / 2)
    if a[m] == n:
        return m
    elif a[m] > n:
        return binary(a, n, 0, m - 1)
    else:
        return binary(a, n, m + 1, r)


a = ["a", "b", "e", "h", "l", "m", "t"]
n = "j"
print(binary(a, n, 0, len(a) - 1))
