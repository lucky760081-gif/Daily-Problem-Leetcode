class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)

        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        dp = {}

        def dfs(i, m):
            if i >= n:
                return 0

            if i + 2 * m >= n:
                return suffix[i]

            if (i, m) in dp:
                return dp[(i, m)]

            best = 0

            for x in range(1, 2 * m + 1):
                best = max(
                    best,
                    suffix[i] - dfs(i + x, max(m, x))
                )

            dp[(i, m)] = best
            return best

        return dfs(0, 1)