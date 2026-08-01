class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        dp = nums[:]

        for length in range(2, n + 1):
            ndp = [0] * (n - length + 1)

            for l in range(n - length + 1):
                r = l + length - 1

                ndp[l] = max(
                    nums[l] - dp[l + 1],
                    nums[r] - dp[l]
                )

            dp = ndp

        return dp[0] >= 0