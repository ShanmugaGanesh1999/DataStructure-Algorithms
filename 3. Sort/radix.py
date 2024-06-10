import math


def getDigit(n, d):
    return int((abs(n) / (10**d)) % 10)


def digitCount(n):
    if n == 0:
        return 1
    return int(math.log10(abs(n)) + 1)


def mostDigit(a):
    m = 0
    for i in a:
        t = digitCount(i)
        if m < t:
            m = t
    return m


def radix(a):
    largestDigit = mostDigit(a)
    for i in range(largestDigit):
        bucket = [[] for _ in range(10)]
        for j in range(len(a)):
            idx = getDigit(a[j], i)
            bucket[idx].append(a[j])
        a = [item for sublist in bucket for item in sublist]
    return a


print(radix([10, 2, 67, 45, 2345, 654]))
