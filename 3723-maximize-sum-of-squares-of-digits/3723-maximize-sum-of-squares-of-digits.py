class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if sum > 9 * num:
            return ""

        digits = [0] * num

        for i in range(num):
            digit = min(9, sum)
            digits[i] = digit
            sum -= digit

        return "".join(map(str, digits))