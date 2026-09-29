class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        if (m + n - 1) % 2:
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                cur = set()

                if i > 0:
                    cur |= dp[i - 1][j]
                if j > 0:
                    cur |= dp[i][j - 1]

                if grid[i][j] == '(':
                    dp[i][j] = {x + 1 for x in cur if x + 1 <= m + n}
                else:
                    dp[i][j] = {x - 1 for x in cur if x > 0}

        return 0 in dp[m - 1][n - 1]