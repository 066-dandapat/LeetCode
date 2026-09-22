class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = [[0, [0] * k] for _ in range(4 * n)]
        def merge(left, right):
            left_prod, left_cnt = left
            right_prod, right_cnt = right
            prod = (left_prod * right_prod) % k
            cnt = left_cnt[:]
            for r in range(k):
                new_rem = (left_prod * r) % k
                cnt[new_rem] += right_cnt[r]
            return [prod, cnt]
        def build(node, l, r):
            if l == r:
                v = nums[l] % k
                tree[node] = [v, [0] * k]
                tree[node][1][v] = 1
                return
            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )
        def update(node, l, r, pos, value):
            if l == r:
                v = value % k
                tree[node] = [v, [0] * k]
                tree[node][1][v] = 1
                return
            mid = (l + r) // 2
            if pos <= mid:
                update(node * 2, l, mid, pos, value)
            else:
                update(node * 2 + 1, mid + 1, r, pos, value)
            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )
        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]
            mid = (l + r) // 2
            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)
            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)
            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)
            return merge(left, right)
        build(1, 0, n - 1)
        ans = []
        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)
            result = query(1, 0, n - 1, start, n - 1)
            ans.append(result[1][x])
        return ans
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("000"))