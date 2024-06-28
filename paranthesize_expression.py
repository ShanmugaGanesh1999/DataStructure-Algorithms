def evaluate(a, b, op):
    if op == "+":
        return a + b
    elif op == "×":
        return a * b


def recurrence_relation(i, j, x, o, dp, choice):
    if i == j:
        return (x[i], None)

    max_value = float("-inf")
    optimal_k = None

    for k in range(i, j):
        left_value = dp[i][k]
        right_value = dp[k + 1][j]
        current_value = evaluate(left_value, right_value, o[k])

        if current_value > max_value:
            max_value = current_value
            optimal_k = k

    return (max_value, optimal_k)


def compute_max_value(x, o):
    n = len(x)
    dp = [[0] * n for _ in range(n)]
    choice = [[None] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = x[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j], choice[i][j] = recurrence_relation(i, j, x, o, dp, choice)

    return dp[0][n - 1]


x, o = [3, 4, 2, 6, 0.5], ["+", "×", "+", "×"]
print(f"Maximum value of the expression: {compute_max_value(x, o)}")
