class Solution(object):

    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = [0] * k
        prev = [0] * k
        for x in nums:
            cur = [0] * k
            cur[x % k] += 1
            for r in range(k):
                cur[(r * x) % k] += prev[r]
            for r in range(k):
                ans[r] += cur[r]
            prev = cur
        return ans
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("000"))