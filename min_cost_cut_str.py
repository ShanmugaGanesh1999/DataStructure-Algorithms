def min_cost_of_cuts(m, C):
    C = [0] + C + [m]
    n = len(C)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    cuts = [[0 for _ in range(n)] for _ in range(n)]

    for h in range(2, n):
        for i in range(n - h):
            j = i + h
            dp[i][j] = float("inf")
            for k in range(i + 1, j):
                cost = dp[i][k] + dp[k][j] + (C[j] - C[i])
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    cuts[i][j] = k

    def order_of_cuts(i, j):
        if i + 1 == j:
            return []
        else:
            k = cuts[i][j]
            return [k] + order_of_cuts(i, k) + order_of_cuts(k, j)

    return dp[0][n - 1], order_of_cuts(0, n - 1)


m, C = 20, [3, 10, 14]
min_cost, order_of_cuts = min_cost_of_cuts(m, C)
print(f"Minimum cost: {min_cost}\nOrder of cuts: {order_of_cuts}")
