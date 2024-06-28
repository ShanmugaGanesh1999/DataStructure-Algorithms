# Θ(n)
def find_target(a: list, b: list, x: int) -> list:
    pairs = []
    i, j = 0, len(b) - 1
    n = len(a)

    while i < n and j >= 0:
        sum = a[i] + b[j]
        if x == sum:
            pairs.append((i, j))
            i += 1
            j -= 1
        elif x < sum:
            j -= 1
        else:
            i += 1

    return False if len(pairs) == 0 else pairs


a = [1, 3, 5, 7, 9]  # odd sorted list
b = [2, 4, 6, 8]  # even sorted list
x = 13  # target value
print(
    a, b, x, find_target(a, b, x), sep="\n"
)  # returns [(i,j)] if a[i]+b[j] == x else false
