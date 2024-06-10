"""
# O(n) - helper recursive approach
def collectOddNumbers(a):
    result = []

    def helper(a):
        if len(a) == 0:
            return
        if a[0] % 2 == 1:
            result.append(a[0])
        return helper(a[1:])

    helper(a)
    return result
"""


# O(n)
def collectOddNumbers(a):
    result = []
    if len(a) == 0:
        return result
    if a[0] % 2 == 1:
        result.append(a[0])
    result = result + collectOddNumbers(a[1:])
    return result


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(collectOddNumbers(a))
