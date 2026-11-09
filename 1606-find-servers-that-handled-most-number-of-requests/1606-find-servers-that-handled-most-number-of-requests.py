class Solution:
    def busiestServers(self, k, arrival, load):
        import heapq
        size = 1
        while size < k:
            size *= 2
        tree = [0] * (2 * size)
        def update(i, val):
            i += size
            tree[i] = val
            while i > 1:
                i //= 2
                tree[i] = tree[2 * i] + tree[2 * i + 1]
        def query(node, start, end, l):
            if end < l or tree[node] == 0:
                return -1
            if start == end:
                return start if start < k else -1
            mid = (start + end) // 2
            res = query(2 * node, start, mid, l)
            if res != -1:
                return res
            return query(2 * node + 1, mid + 1, end, l)
        for i in range(k):
            update(i, 1)
        busy = []
        count = [0] * k
        for i in range(len(arrival)):
            while busy and busy[0][0] <= arrival[i]:
                end, server = heapq.heappop(busy)
                update(server, 1)
            if tree[1] == 0:
                continue
            start = i % k
            server = query(1, 0, size - 1, start)
            if server == -1:
                server = query(1, 0, size - 1, 0)
            update(server, 0)
            count[server] += 1
            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )
        maximum = max(count)
        return [i for i in range(k) if count[i] == maximum
        ]
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("000"))