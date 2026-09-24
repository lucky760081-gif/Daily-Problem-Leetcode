class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            n = nums[i]
            digit_sum = 0

            while n:
                digit_sum += n % 10
                n //= 10

            if digit_sum == i:
                return i

        return -1