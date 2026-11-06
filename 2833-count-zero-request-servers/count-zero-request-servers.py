class Solution(object):
    def countServers(self, n, logs, x, queries):
        """
        :type n: int
        :type logs: List[List[int]]
        :type x: int
        :type queries: List[int]
        :rtype: List[int]
        """
        logs.sort(key=lambda p: p[1])
        indexed = sorted((q, i) for i, q in enumerate(queries))

        count = [0] * (n + 1)
        ans = [0] * len(queries)

        left = right = active = 0

        for q, idx in indexed:
            while right < len(logs) and logs[right][1] <= q:
                s, t = logs[right]
                if count[s] == 0:
                    active += 1
                count[s] += 1
                right += 1

            while left < right and logs[left][1] < q - x:
                s, t = logs[left]
                count[s] -= 1
                if count[s] == 0:
                    active -= 1
                left += 1

            ans[idx] = n - active

        return ans