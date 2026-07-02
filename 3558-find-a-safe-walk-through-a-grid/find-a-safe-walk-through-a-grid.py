class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])

        dist = [[float('inf')] * n for _ in range(m)]
        cost = grid[0][0]
        dist[0][0] = cost

        pq = [(cost, 0, 0)]
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while pq:
            c, x, y = heappop(pq)

            if c > dist[x][y]:
                continue

            if x == m - 1 and y == n - 1:
                return c < health

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nc = c + grid[nx][ny]
                    if nc < dist[nx][ny]:
                        dist[nx][ny] = nc
                        heappush(pq, (nc, nx, ny))

        return False