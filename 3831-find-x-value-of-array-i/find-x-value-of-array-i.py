class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dp = [0] * k
        ans = [0] * k

        for num in nums:
            r = num % k
            new = [0] * k

            new[r] += 1

            for p in range(k):
                if dp[p]:
                    new[(p * r) % k] += dp[p]

            dp = new

            for p in range(k):
                ans[p] += dp[p]

        return ans