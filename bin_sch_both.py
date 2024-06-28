def compare_strings(x, y):
    return -1 if x < y else 1 if x > y else 0


def partition(C, pivot):
    pivot_index = 0

    for i, string in enumerate(C):
        if string == pivot:
            pivot_index = i
            break

    C[0], C[pivot_index] = C[pivot_index], C[0]

    i = 1
    for j in range(1, len(C)):
        if compare_strings(C[j], pivot) < 0:
            C[i], C[j] = C[j], C[i]
            i += 1

    C[0], C[i - 1] = C[i - 1], C[0]

    return i - 1


def find_missing(D, C):
    if len(D) == 1:
        return D[0]

    mid_index = len(D) // 2
    pivot = D[mid_index]
    pivot_index = partition(C, pivot)

    if pivot_index >= len(C) or C[pivot_index] != pivot:
        return pivot

    if pivot_index < mid_index:
        return find_missing(D[:mid_index], C[:pivot_index])
    return find_missing(D[mid_index + 1 :], C[pivot_index + 1 :])


D = ["coffee", "kombucha", "slushy", "soda", "tea"]
C = ["kombucha", "tea", "soda", "coffee"]
missing_string = find_missing(D, C)
print("The missing string in C: ", missing_string)
