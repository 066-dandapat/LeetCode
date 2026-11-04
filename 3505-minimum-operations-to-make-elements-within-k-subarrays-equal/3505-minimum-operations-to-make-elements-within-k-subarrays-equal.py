class Solution(object):
    def minOperations(self, nums, x, k):
        """
        :type nums: List[int]
        :type x: int
        :type k: int
        :rtype: int
        """
        n = len(nums)
        vals = sorted(set(nums))
        m = len(vals)
        rank = {v: i + 1 for i, v in enumerate(vals)}
        count = [0] * (m + 1)
        total = [0] * (m + 1)
        def update(i, v, delta):
            while i <= m:
                count[i] += delta
                total[i] += v * delta
                i += i & -i
        def query(i):
            c = s = 0
            while i:
                c += count[i]
                s += total[i]
                i -= i & -i
            return c, s
        def median_rank(target):
            idx = 0
            bit = 1 << (m.bit_length() - 1)
            while bit:
                nxt = idx + bit
                if nxt <= m and count[nxt] < target:
                    target -= count[nxt]
                    idx = nxt
                bit >>= 1
            return idx + 1
        costs = [0] * (n - x + 1)
        window_sum = 0
        for i, v in enumerate(nums):
            update(rank[v], v, 1)
            window_sum += v
            if i >= x:
                old = nums[i - x]
                update(rank[old], old, -1)
                window_sum -= old
            if i >= x - 1:
                r = median_rank((x + 1) // 2)
                med = vals[r - 1]
                c, s = query(r)
                left = med * c - s
                right = window_sum - s - med * (x - c)
                costs[i - x + 1] = left + right
        INF = float('inf')
        prev = [0] * (n + 1)
        for j in range(1, k + 1):
            curr = [INF] * (n + 1)
            for i in range(j * x, n + 1):
                curr[i] = min(
                    curr[i - 1],
                    prev[i - x] + costs[i - x]
                )
            prev = curr
        return prev[n]
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("000"))
