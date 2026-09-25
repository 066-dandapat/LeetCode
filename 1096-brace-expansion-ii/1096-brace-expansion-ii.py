class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """

        def parse(s, i):
            result = set()
            current = {""}

            while i < len(s) and s[i] != '}':
                if s[i] == '{':
                    sub, i = parse(s, i + 1)
                    current = {a + b for a in current for b in sub}

                elif s[i] == ',':
                    result.update(current)
                    current = {""}
                    i += 1

                else:
                    ch = s[i]
                    current = {x + ch for x in current}
                    i += 1

            result.update(current)

            return result, i + 1

        result, _ = parse(expression, 0)

        return sorted(result)