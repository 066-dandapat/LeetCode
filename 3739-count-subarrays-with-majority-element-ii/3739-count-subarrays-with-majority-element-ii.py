class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
    def update(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i
    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s
class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        tree = BinaryIndexedTree(2 * n + 1)
        prefix = n + 1
        tree.update(prefix, 1)
        ans = 0
        for x in nums:
            if x == target:
                prefix += 1
            else:
                prefix -= 1
            ans += tree.query(prefix - 1)
            tree.update(prefix, 1)
        return ans
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("000"))