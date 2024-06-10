"""
# O(2^n)
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)
"""

"""
# memorization - O(n) - top down (recursion)
def fibonacci(n):
    array = [None] * (n + 1)

    def fib(n):
        if array[n] != None:
            return array[n]
        if n <= 2:
            return 1
        res = fib(n - 1) + fib(n - 2)
        array[n] = res
        return res

    return fib(n)
"""


# tabulation - O(n) - bottom up (iteration) - easy on space complexity
def fibonacci(n):
    array = [0, 1]
    for i in range(2, n + 1):
        array.append(array[i - 1] + array[i - 2])
    return array[n]


# print(fib(45))  # 132 sec
print(fibonacci(45))  # 1 sec
