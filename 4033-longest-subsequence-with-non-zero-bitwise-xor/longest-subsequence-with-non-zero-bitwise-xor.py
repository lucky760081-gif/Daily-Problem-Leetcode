class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_xor = 0

        for x in nums:
            total_xor ^= x

        n = len(nums)

        if total_xor != 0:
            return n

        for x in nums:
            if x != 0:
                return n - 1

        return 0
        