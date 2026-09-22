class Solution(object):
    def resultArray(self, nums, k, queries):
        """
        :type nums: List[int]
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        size = 1

        while size < n:
            size *= 2

        tree = [[0] * k for _ in range(2 * size)]
        prod = [1] * (2 * size)

        def build(pos, val):
            p = val % k
            prod[pos] = p
            tree[pos][p] = 1

        def merge(pos):
            left = pos * 2
            right = left + 1

            lp = prod[left]
            prod[pos] = (lp * prod[right]) % k

            a = tree[left]
            b = tree[right]
            cur = tree[pos]

            for i in range(k):
                cur[i] = a[i]

            for i in range(k):
                if b[i]:
                    cur[(lp * i) % k] += b[i]

        for i in range(n):
            build(size + i, nums[i])

        for i in range(size - 1, 0, -1):
            merge(i)

        def update(idx, val):
            p = size + idx

            for i in range(k):
                tree[p][i] = 0

            prod[p] = val % k
            tree[p][prod[p]] = 1

            p //= 2

            while p:
                merge(p)
                p //= 2

        def query(l):
            left_nodes = []
            right_nodes = []

            l += size
            r = size + n

            while l < r:
                if l & 1:
                    left_nodes.append(l)
                    l += 1

                if r & 1:
                    r -= 1
                    right_nodes.append(r)

                l //= 2
                r //= 2

            nodes = left_nodes + right_nodes[::-1]

            result = [0] * k
            current_prod = 1

            for node in nodes:
                p = current_prod
                arr = tree[node]

                for x in range(k):
                    if arr[x]:
                        result[(p * x) % k] += arr[x]

                current_prod = (current_prod * prod[node]) % k

            return result

        ans = []

        for index, value, start, x in queries:
            update(index, value)
            cnt = query(start)
            ans.append(cnt[x])

        return ans