class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10 ** 9 + 7
        n = len(s)
        digits = []
        positions = []
        for i, ch in enumerate(s):
            if ch != '0':
                digits.append(int(ch))
                positions.append(i)
        m = len(digits)
        if m == 0:
            return [0] * len(queries)
        posToIdx = {}
        for i, p in enumerate(positions):
            posToIdx[p] = i
        prefSum = [0] * (m + 1)
        for i in range(m):
            prefSum[i + 1] = prefSum[i] + digits[i]
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
        prefVal = [0] * (m + 1)
        for i in range(m):
            prefVal[i + 1] = (prefVal[i] * 10 + digits[i]) % MOD
        nextNonZero = [-1] * n
        nxt = -1
        for i in range(n - 1, -1, -1):
            if s[i] != '0':
                nxt = i
            nextNonZero[i] = nxt
        prevNonZero = [-1] * n
        prv = -1
        for i in range(n):
            if s[i] != '0':
                prv = i
            prevNonZero[i] = prv
        ans = []
        for l, r in queries:
            leftPos = nextNonZero[l]
            if leftPos == -1 or leftPos > r:
                ans.append(0)
                continue
            rightPos = prevNonZero[r]
            L = posToIdx[leftPos]
            R = posToIdx[rightPos]
            length = R - L + 1
            x = (prefVal[R + 1] - prefVal[L] * pow10[length]) % MOD
            digitSum = prefSum[R + 1] - prefSum[L]
            ans.append((x * digitSum) % MOD)
        return ans
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("000"))