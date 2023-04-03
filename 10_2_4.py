def knapsack(weights, values, max_weight):
    n = len(weights)
    dp = [0] * (max_weight + 1)
    for i in range(n):
        for j in range(max_weight, weights[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
    return dp[max_weight]

# Пример использования функции
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
max_weight = 8
max_value = knapsack(weights, values, max_weight)
print("Максимальная стоимость, которую можно унести в рюкзаке:", max_value)
