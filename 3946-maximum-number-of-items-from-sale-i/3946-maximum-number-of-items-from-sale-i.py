class Solution:
    def maximumSaleItems(self, items, budget):
        n = len(items)
        dp = [0] * (budget + 1)

        for i in range(n):
            f, p = items[i]

            free = 0
            for j in range(n):
                if i != j and items[j][0] % f == 0:
                    free += 1

            buy = [-10**9] * (budget + 1)

            for c in range(p, budget + 1):
                buy[c] = max(
                    dp[c - p] + free + 1,
                    buy[c - p] + 1
                )

            for c in range(budget + 1):
                dp[c] = max(dp[c], buy[c])

        return max(dp)