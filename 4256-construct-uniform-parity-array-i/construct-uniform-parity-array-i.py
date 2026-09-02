class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        n = len(nums1)

        if n == 1:
            return True

        even = sum(x % 2 == 0 for x in nums1)
        odd = n - even

        if even == n or odd == n:
            return True

        if even >= 1 and odd >= 1:
            return True

        return False