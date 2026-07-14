class Solution(object):
    def subsequencePairCount(self, nums):
        from functools import lru_cache

        MOD = 1000000007
        n = len(nums)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        @lru_cache(None)
        def dfs(i, g1, g2):
            if i == n:
                return 1 if g1 == g2 and g1 != 0 else 0

            x = nums[i]

            ans = dfs(i + 1, g1, g2)

            if g1 == 0:
                ans += dfs(i + 1, x, g2)
            else:
                ans += dfs(i + 1, gcd(g1, x), g2)

            if g2 == 0:
                ans += dfs(i + 1, g1, x)
            else:
                ans += dfs(i + 1, g1, gcd(g2, x))

            return ans % MOD

        return dfs(0, 0, 0)