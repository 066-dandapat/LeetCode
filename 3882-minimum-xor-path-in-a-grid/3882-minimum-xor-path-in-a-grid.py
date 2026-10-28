class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = {grid[i][j]}
                    continue

                prev = set()

                if i > 0:
                    prev.update(dp[j])

                if j > 0:
                    prev.update(dp[j - 1])

                dp[j] = {x ^ grid[i][j] for x in prev}

        return min(dp[-1])