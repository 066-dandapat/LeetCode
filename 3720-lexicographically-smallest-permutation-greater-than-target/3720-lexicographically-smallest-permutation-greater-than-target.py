class Solution(object):
    def lexGreaterPermutation(self, s, target):
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        ans = []

        # Try to match target from left to right
        for i in range(len(target)):
            x = ord(target[i]) - ord('a')

            if cnt[x] > 0:
                cnt[x] -= 1
                ans.append(target[i])
            else:
                # Find smallest character greater than target[i]
                found = False

                for c in range(x + 1, 26):
                    if cnt[c] > 0:
                        ans.append(chr(c + ord('a')))
                        cnt[c] -= 1

                        # Add remaining characters in sorted order
                        for j in range(26):
                            ans += [chr(j + ord('a'))] * cnt[j]

                        return ''.join(ans)

                found = False
                break

        # Backtrack
        for i in range(len(ans) - 1, -1, -1):
            old = ord(ans[i]) - ord('a')
            cnt[old] += 1

            for c in range(old + 1, 26):
                if cnt[c] > 0:
                    result = ans[:i]
                    result.append(chr(c + ord('a')))
                    cnt[c] -= 1

                    # Remaining characters in sorted order
                    for j in range(26):
                        result += [chr(j + ord('a'))] * cnt[j]

                    return ''.join(result)

        return ""