
class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        # Check if the string is already sorted
        if s == ''.join(sorted(s)):
            return 0

        # A reversed string of length 2 cannot be sorted
        if n == 2:
            return -1

        mn = min(s)
        mx = max(s)

        # One operation is sufficient
        if s[0] == mn or s[-1] == mx:
            return 1

        # Check whether min or max is in the middle
        for i in range(1, n - 1):
            if s[i] == mn or s[i] == mx:
                return 2

        # Both extremes are at the wrong ends
        return 3
