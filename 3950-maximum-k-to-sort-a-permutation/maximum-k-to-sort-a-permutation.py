class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = -1
        for i, x in enumerate(nums):
            if i != x:
                k &= x
        return max(k, 0) if k != -1 else 0