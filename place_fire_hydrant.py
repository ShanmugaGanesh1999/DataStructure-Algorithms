def place_hydrants(X, d):
    X.sort()

    num_hydrants = 0
    i, n = 0, len(X)

    while i < n:
        j = i
        while j < n and X[j] <= X[i] + d:
            j += 1

        hydrant_position = X[j - 1] + d
        num_hydrants += 1

        i = j
        while i < n and X[i] <= hydrant_position:
            i += 1

    return num_hydrants + 1


X, d = [1, 2, 5, 4, 8, 7, 10], 2
print("Number of hydrants needed:", place_hydrants(X, d))
