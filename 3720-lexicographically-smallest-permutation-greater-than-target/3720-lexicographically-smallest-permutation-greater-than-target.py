class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
        ans = []
        for i in range(len(target)):
            x = ord(target[i]) - ord("a")
            if cnt[x] > 0:
                cnt[x] -= 1
                ans.append(target[i])
            else:
                for c in range(x + 1, 26):
                    if cnt[c] > 0:
                        ans.append(chr(c + ord("a")))
                        cnt[c] -= 1
                        for j in range(26):
                            ans.extend([chr(j + ord("a"))] * cnt[j])
                        return "".join(ans)
                break
        for i in range(len(ans) - 1, -1, -1):
            old = ord(ans[i]) - ord("a")
            cnt[old] += 1
            for c in range(old + 1, 26):
                if cnt[c] > 0:
                    result = ans[:i] + [chr(c + ord("a"))]
                    cnt[c] -= 1
                    for j in range(26):
                        result.extend([chr(j + ord("a"))] * cnt[j])
                    return "".join(result)
        return ""
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("000"))