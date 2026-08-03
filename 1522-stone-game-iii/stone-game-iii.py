class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)

        dp = [0] * (n + 3)

        for i in range(n - 1, -1, -1):
            take = 0
            dp[i] = -10**18

            for k in range(3):
                if i + k < n:
                    take += stoneValue[i + k]
                    dp[i] = max(dp[i], take - dp[i + k + 1])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"