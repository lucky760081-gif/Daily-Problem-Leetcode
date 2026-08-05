class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        g = [[] for _ in range(n)]

        for u, v in invocations:
            g[u].append(v)

        suspicious = [False] * n
        q = deque([k])
        suspicious[k] = True

        while q:
            u = q.popleft()
            for v in g[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    q.append(v)

        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        return [i for i in range(n) if not suspicious[i]]