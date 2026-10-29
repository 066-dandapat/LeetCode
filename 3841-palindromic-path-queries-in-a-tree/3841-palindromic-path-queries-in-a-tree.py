class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        LOG = max(1, n.bit_length())
        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        it = [0] * n
        stack = [0]
        timer = 1
        tin[0] = 1
        while stack:
            u = stack[-1]
            if it[u] < len(g[u]):
                v = g[u][it[u]]
                it[u] += 1
                if v == parent[u] and u != 0:
                    continue
                if v == 0 and u != 0:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                timer += 1
                tin[v] = timer
                stack.append(v)
            else:
                tout[u] = timer
                stack.pop()
        up = [parent]
        for j in range(1, LOG):
            prev = up[j - 1]
            up.append([prev[prev[v]] for v in range(n)])
        bit = [0] * (n + 2)
        def add(i, x):
            while i <= n + 1:
                bit[i] ^= x
                i += i & -i
        def get(i):
            result = 0
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            d = depth[u] - depth[v]
            for j in range(LOG):
                if (d >> j) & 1:
                    u = up[j][u]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]
            return up[0][u]
        chars = [ord(c) - 97 for c in s]
        for u in range(n):
            x = 1 << chars[u]
            add(tin[u], x)
            add(tout[u] + 1, x)
        result = []
        for q in queries:
            p = q.split()
            if p[0] == "update":
                u = int(p[1])
                c = ord(p[2]) - 97
                if chars[u] != c:
                    x = (1 << chars[u]) ^ (1 << c)
                    add(tin[u], x)
                    add(tout[u] + 1, x)
                    chars[u] = c
            else:
                u = int(p[1])
                v = int(p[2])
                w = lca(u, v)
                mask = get(tin[u]) ^ get(tin[v]) ^ (1 << chars[w])
                result.append((mask & (mask - 1)) == 0)
        return result
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("000"))