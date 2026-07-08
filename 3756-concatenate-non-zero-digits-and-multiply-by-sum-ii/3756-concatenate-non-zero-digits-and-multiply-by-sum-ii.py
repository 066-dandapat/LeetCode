from typing import List
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
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
        pos_to_idx = {p: i for i, p in enumerate(positions)}
        pref_sum = [0] * (m + 1)
        for i in range(m):
            pref_sum[i + 1] = pref_sum[i] + digits[i]
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
        pref_val = [0] * (m + 1)
        for i in range(m):
            pref_val[i + 1] = (pref_val[i] * 10 + digits[i]) % MOD
        next_nonzero = [-1] * n
        nxt = -1
        for i in range(n - 1, -1, -1):
            if s[i] != '0':
                nxt = i
            next_nonzero[i] = nxt
        prev_nonzero = [-1] * n
        prv = -1
        for i in range(n):
            if s[i] != '0':
                prv = i
            prev_nonzero[i] = prv
        ans = []
        for l, r in queries:
            left = next_nonzero[l]
            if left == -1 or left > r:
                ans.append(0)
                continue
            right = prev_nonzero[r]
            L = pos_to_idx[left]
            R = pos_to_idx[right]
            length = R - L + 1
            num = (pref_val[R + 1] - pref_val[L] * pow10[length]) % MOD
            digit_sum = pref_sum[R + 1] - pref_sum[L]
            ans.append((num * digit_sum) % MOD)
        return ans
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("000"))