def delta(xi, yj):
    return 0 if xi == yj else 1


def recurrence_relation(i, j, X, Y, dp):
    if i == 0:
        return (j, "ins")
    elif j == 0:
        return (i, "del")

    delCost = dp[i - 1][j] + 1
    insCost = dp[i][j - 1] + 1
    subCost = dp[i - 1][j - 1] + delta(X[i - 1], Y[j - 1])

    minCost = min(delCost, insCost, subCost)

    if minCost == delCost:
        action = "del"
    elif minCost == insCost:
        action = "ins"
    else:
        action = "sub"

    return (minCost, action)


def compute_edit_distance(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    choice = [[None] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            dp[i][j], choice[i][j] = recurrence_relation(i, j, X, Y, dp)

    return dp[m][n], choice


def reconstruct_operations(choice, X, Y):
    i = len(X)
    j = len(Y)
    operations = []

    while i > 0 or j > 0:
        action = choice[i][j]
        if action == "del":
            operations.append(f"delete {X[i - 1]}")
            i -= 1
        elif action == "ins":
            operations.append(f"insert {Y[j - 1]}")
            j -= 1
        elif action == "sub":
            if X[i - 1] != Y[j - 1]:
                operations.append(f"substitute {X[i - 1]} with {Y[j - 1]}")
            i -= 1
            j -= 1

    return operations[::-1]


X, Y = "esteban", "stephen"
edit_distance, choice = compute_edit_distance(X, Y)

print(f"Edit distance between '{X}' and '{Y}': {edit_distance}")
print("Operations to convert X to Y:")
for operation in reconstruct_operations(choice, X, Y):
    print(operation)
