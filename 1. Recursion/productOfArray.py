# O(n)
def multiplication(n):
    if len(n) == 0:
        return 1
    return n[0] * multiplication(n[1:])


n = [1, 2, 3, 4, 5]  # 120
print(multiplication(n))
