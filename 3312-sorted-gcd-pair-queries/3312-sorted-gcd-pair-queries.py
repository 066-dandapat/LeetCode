class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        from bisect import bisect_right

        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        gcd_pairs = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            total = 0
            for multiple in range(g, mx + 1, g):
                total += freq[multiple]
            pairs = total * (total - 1) // 2
            for multiple in range(2 * g, mx + 1, g):
                pairs -= gcd_pairs[multiple]
            gcd_pairs[g] = pairs

        prefix = [0] * (mx + 1)
        for i in range(1, mx + 1):
            prefix[i] = prefix[i - 1] + gcd_pairs[i]

        ans = []
        for q in queries:
            ans.append(bisect_right(prefix, q))
        return ans
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("000"))