# O(n) - frequency counter
def anagram(a: str, b: str):
    if len(a) != len(b):
        return False
    m = {i: a.count(i) for i in a}
    for i in b:
        if not m.get(i):
            return False
        else:
            m[i] -= 1
    return True


# a, b = "dog", "god"  # true
# a, b = "aaz", "zza"  # false
a, b = "aaz", "zaas"  # false
print(anagram(a, b))
