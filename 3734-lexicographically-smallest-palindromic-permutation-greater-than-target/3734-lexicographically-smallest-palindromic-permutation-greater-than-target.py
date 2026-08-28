class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        # Check palindrome possibility
        odd = 0
        middle = ""

        for i in range(26):
            if cnt[i] % 2:
                odd += 1
                middle = chr(i + 97)

        if odd > 1:
            return ""

        # Counts for the left half
        half = [0] * 26
        for i in range(26):
            half[i] = cnt[i] // 2

        m = n // 2
        left = []

        for pos in range(m):
            found = False

            for c in range(26):
                if half[c] == 0:
                    continue

                half[c] -= 1
                left.append(chr(c + 97))

                # Make the largest possible palindrome
                temp = left[:]

                for x in range(25, -1, -1):
                    if half[x] > 0:
                        temp.extend([chr(x + 97)] * half[x])

                L = ''.join(temp)
                candidate = L + middle + L[::-1]

                if candidate > target:
                    found = True
                    break

                # Undo choice
                left.pop()
                half[c] += 1

            if not found:
                return ""

        L = ''.join(left)
        ans = L + middle + L[::-1]
        if ans <= target:
            return ""
        return ans