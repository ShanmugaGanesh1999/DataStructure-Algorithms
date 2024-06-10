def searchCount(a, b):
    c = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i + j] != b[j]:
                break
            if j == len(b) - 1:
                c += 1
    return c


a, b = "lollorie loled", "lol"
print(searchCount(a, b))
