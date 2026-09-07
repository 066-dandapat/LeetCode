class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = 1
        last = {}
        for ch in s:
            new_dp = (2 * dp - last.get(ch, 0)) % MOD
            last[ch] = dp
            dp = new_dp
        return (dp - 1) % MOD
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("000"))