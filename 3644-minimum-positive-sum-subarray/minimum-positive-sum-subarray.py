class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        n = len(nums)
        ans = float('inf')

        for i in range(n):
            total = 0
            for j in range(i, min(n, i + r)):
                total += nums[j]
                if l <= j - i + 1 <= r and total > 0:
                    ans = min(ans, total)

        return ans if ans != float('inf') else -1