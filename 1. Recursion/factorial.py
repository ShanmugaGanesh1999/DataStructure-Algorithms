# O(n)
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


# n = 4  # 24
n = 5  # 120
print(factorial(n))
