# O(n)
def fibonacci(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


n = 12
print(fibonacci(n))
# 0,1,2,3,4,5,6, 7, 8, 9,10,11, 12
# 0,1,1,2,3,5,8,13,21,34,55,89,144
