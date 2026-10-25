class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        ans = 0

        def dfs(r, c):
            stack = [(r, c)]
            grid[r][c] = 1
            closed = True

            while stack:
                x, y = stack.pop()

                if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                    closed = False

                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        stack.append((nx, ny))

            return closed

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0 and dfs(i, j):
                    ans += 1

        return ans