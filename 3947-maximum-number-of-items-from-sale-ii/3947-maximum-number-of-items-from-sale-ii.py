class Solution(object):
    def maximumSaleItems(self, items, budget):
        """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
        n = len(items)

        min_price = min(price for factor, price in items)
        max_factor = max(factor for factor, price in items)

        # Count occurrences of each factor
        freq = [0] * (max_factor + 1)

        for factor, price in items:
            freq[factor] += 1

        # Count items whose factors are multiples of each factor
        total = freq[:]

        for i in range(1, max_factor + 1):
            for j in range(2 * i, max_factor + 1, i):
                total[i] += freq[j]

        # Collect bonus purchases grouped by price
        bonus = {}

        for factor, price in items:
            gifts = total[factor] - 1

            if gifts > 0 and price < 2 * min_price:
                bonus[price] = bonus.get(price, 0) + gifts

        # Buy the cheapest bonus purchases first
        ans = 0

        for price in sorted(bonus):
            if budget < price:
                break

            take = min(bonus[price], budget // price)

            ans += 2 * take
            budget -= take * price

        # Buy regular items using remaining budget
        ans += budget // min_price

        return ans