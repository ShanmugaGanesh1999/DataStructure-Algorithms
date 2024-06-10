# O(n)
def exponent(n, e):
    if n == 1 or e == 0:
        return 1
    return n * exponent(n, e - 1)


n, e = 3, 3
print(exponent(n, e))
