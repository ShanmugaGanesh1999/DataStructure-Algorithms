def local_minimum(a, l, r) -> int:
    if l == r:
        return l

    m = int((l + r) / 2)

    if (m == 0 or a[m] < a[m - 1]) and (m == len(a) - 1 or a[m] < a[m + 1]):
        return m

    if m > 0 and a[m] > a[m - 1]:
        return local_minimum(a, l, m - 1)

    return local_minimum(a, m + 1, r)


# index starts with 0

a = [6, 3, 4, 7, 9, 11]

print(f"local minimum index: {local_minimum(a, 0, len(a) - 1)}")
