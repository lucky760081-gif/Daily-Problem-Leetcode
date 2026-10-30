class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :type k: int
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        if n == 1:
            return 0

        INF = 10**18
        dist = [[INF] * (k + 1) for _ in range(n)]
        dist[0][1] = 0

        pq = [(0, 0, 1)]

        while pq:
            cost, u, cnt = heapq.heappop(pq)

            if cost != dist[u][cnt]:
                continue

            if u == n - 1:
                return cost

            for v, w in adj[u]:
                if labels[u] == labels[v]:
                    if cnt == k:
                        continue
                    nc = cnt + 1
                else:
                    nc = 1

                new_cost = cost + w

                if new_cost < dist[v][nc]:
                    dist[v][nc] = new_cost
                    heapq.heappush(pq, (new_cost, v, nc))

        return -1