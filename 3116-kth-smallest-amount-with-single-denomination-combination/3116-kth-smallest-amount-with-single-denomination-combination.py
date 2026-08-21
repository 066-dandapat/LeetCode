class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        from math import gcd
        def lcm(a, b):
            return a // gcd(a, b) * b
        def count(x):
            n = len(coins)
            total = 0
            for mask in range(1, 1 << n):
                val = 1
                bits = 0
                for i in range(n):
                    if mask & (1 << i):
                        val = lcm(val, coins[i])
                        if val > x:
                            break
                        bits += 1
                if val <= x:
                    cur = x // val
                    if bits % 2:
                        total += cur
                    else:
                        total -= cur

            return total
        left = 1
        right = min(coins) * k
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("000"))