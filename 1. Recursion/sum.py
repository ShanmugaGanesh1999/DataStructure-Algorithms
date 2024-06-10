# O(n)
def addition(n):
    if n == 1:
        return 1
    return n + addition(n - 1)


n = 10  # 55
print(addition(n))
