class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n + 1)]

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        q = deque([1])
        vis = [False] * (n + 1)
        vis[1] = True
        ans = float('inf')

        while q:
            u = q.popleft()
            for v, w in graph[u]:
                ans = min(ans, w)
                if not vis[v]:
                    vis[v] = True
                    q.append(v)

        return ans