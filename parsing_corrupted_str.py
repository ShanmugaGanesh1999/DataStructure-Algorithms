# θ(1)
def is_word(word):
    meaningful_words = {"all", "work", "no", "play", "makes", "jack", "dull", "boy"}
    return word in meaningful_words


# θ(n^2)
def min_cost_insert_spaces(X):
    n = len(X)
    dp = [float("inf")] * (n + 1)
    split = [-1] * (n + 1)

    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(i):
            word = X[j:i]
            cost = 0 if is_word(word) else i - j
            dp_i, dp_j = dp[i], dp[j]
            dp_j_cost = dp_j + cost
            if dp_j_cost < dp_i:
                dp[i] = dp[j] + cost
                split[i] = j
    i = n
    words = []
    while i > 0:
        j = split[i]
        word = X[j:i]
        words.append(word)
        i = j
    words.reverse()
    return " ".join(words), dp[n]


X = "allworkzkdnoplaymakesjackjdullbiy"
result, cost = min_cost_insert_spaces(X)
print(f"Optimal split: {result}\nTotal cost:{cost}")
