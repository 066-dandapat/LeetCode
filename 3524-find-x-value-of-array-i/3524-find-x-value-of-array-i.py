class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        prev = [0] * k

        for x in nums:
            cur = [0] * k

            # Subarray consisting only of x
            cur[x % k] += 1

            # Extend all subarrays ending at the previous position
            for r in range(k):
                cur[(r * x) % k] += prev[r]

            # Add all subarrays ending at this position
            for r in range(k):
                ans[r] += cur[r]

            prev = cur

        return ans