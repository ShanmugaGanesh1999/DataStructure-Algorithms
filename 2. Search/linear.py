# O(n)
def search(a, n):
    for idx, i in enumerate(a):
        if n == i:
            return idx
    return -1


a = ["p", "c", "q", "e", "r", "t", "a"]
n = "a"
print(search(a, n))
