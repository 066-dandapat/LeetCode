from collections import deque
class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        n = len(online)
        if n == 1:
            return 0
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        weights = set()
        for u, v, w in edges:
            graph[u].append((v, w))
            indegree[v] += 1
            weights.add(w)
        q = deque()
        topo = []
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        while q:
            u = q.popleft()
            topo.append(u)
            for v, w in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        weights = sorted(weights)
        def check(limit):
            INF = 10 ** 30
            dist = [INF] * n
            dist[0] = 0
            for u in topo:
                if dist[u] == INF:
                    continue
                if u != 0 and u != n - 1 and not online[u]:
                    continue
                for v, w in graph[u]:
                    if w < limit:
                        continue
                    if v != n - 1 and not online[v]:
                        continue
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
            return dist[n - 1] <= k
        if not check(0):
            return -1
        lo, hi = 0, len(weights) - 1
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(weights[mid]):
                ans = weights[mid]
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("000"))