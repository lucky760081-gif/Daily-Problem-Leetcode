class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        order = sorted((nums[i], i) for i in range(n))

        # pos[node] = position in sorted order
        pos = [0] * n
        for i, (_, idx) in enumerate(order):
            pos[idx] = i

        # Component id in sorted order
        comp = [0] * n
        cid = 0
        for i in range(1, n):
            if order[i][0] - order[i - 1][0] > maxDiff:
                cid += 1
            comp[i] = cid

        far = [0] * n
        j = 0
        for i in range(n):
            while j + 1 < n and order[j + 1][0] - order[i][0] <= maxDiff:
                j += 1
            far[i] = j

        LOG = (n).bit_length()
        up = [far]
        for _ in range(1, LOG):
            prev = up[-1]
            cur = [0] * n
            for i in range(n):
                cur[i] = prev[prev[i]]
            up.append(cur)

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            pu = pos[u]
            pv = pos[v]

            if pu > pv:
                pu, pv = pv, pu

            if comp[pu] != comp[pv]:
                ans.append(-1)
                continue

            cur = pu
            steps = 0

            for k in range(LOG - 1, -1, -1):
                nxt = up[k][cur]
                if nxt < pv:
                    cur = nxt
                    steps += 1 << k

            ans.append(steps + 1)

        return ans