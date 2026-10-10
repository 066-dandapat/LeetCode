
class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        diff.sort(reverse=True)
        diff.append(0)

        n = len(diff) - 1

        for i in range(n):
            need = (diff[i] - diff[i + 1]) * (i + 1)

            if k >= need:
                k -= need
            else:
                level = diff[i] - k // (i + 1)
                rem = k % (i + 1)

                ans = sum(x * x for x in diff[i + 1:n])

                for j in range(i + 1):
                    if j < rem:
                        ans += (level - 1) ** 2
                    else:
                        ans += level ** 2

                return ans

        return 0
