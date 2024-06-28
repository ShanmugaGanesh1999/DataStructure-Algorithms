def recurrence_relation(k, v, dp):
    for j in range(len(v)):
        if v[j] == k:
            return (1, j)

    min_value = float("inf")
    min_index = -1

    for l in range(len(v)):
        if k - v[l] >= 0:
            current_value = dp[k - v[l]] + 1
            if current_value < min_value:
                min_value = current_value
                min_index = l

    return (min_value, min_index)


def compute_min_coins(v, t):
    dp = [float("inf")] * (t + 1)
    choice = [None] * (t + 1)

    dp[0] = 0

    for k in range(1, t + 1):
        dp[k], choice[k] = recurrence_relation(k, v, dp)

    return dp[t], choice


def reconstruct_solution(choice, v, t):
    result = []

    while t > 0:
        coin_index = choice[t]
        coin_value = v[coin_index]
        result.append(coin_value)
        t -= coin_value

    return result


v, t = [1, 2, 5], 9
min_coins, choice = compute_min_coins(v, t)

print(f"Minimum number of coins needed: {min_coins}")
print(f"Coins used to make change for {t}: {reconstruct_solution(choice, v, t)}")
