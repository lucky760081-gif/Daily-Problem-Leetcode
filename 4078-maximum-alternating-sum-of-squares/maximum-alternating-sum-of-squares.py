class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        squares = sorted([x * x for x in nums], reverse=True)
        n = len(squares)
        positive = (n + 1) // 2
        negative = n // 2

        return sum(squares[:positive]) - sum(squares[n - negative:])