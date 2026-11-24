class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        def lcm(a, b):
            return (a * b) // gcd(a, b)
        ans = 0
        n = len(nums)
        for i in range(n):
            prod = 1
            g = 0
            l = 1
            for j in range(i, n):
                x = nums[j]
                prod *= x
                g = gcd(g, x)
                l = lcm(l, x)
                if prod == g * l:
                    ans = max(ans, j - i + 1)
        return ans