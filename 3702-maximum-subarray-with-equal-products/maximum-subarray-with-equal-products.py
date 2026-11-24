class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0

        for i in range(n):
            prod = 1
            g = 0
            l = 1

            for j in range(i, n):
                x = nums[j]
                prod *= x

                a, b = g, x
                while b:
                    a, b = b, a % b
                g = a

                a, b = l, x
                while b:
                    a, b = b, a % b
                l = l * x // a

                if prod == l * g:
                    ans = max(ans, j - i + 1)

        return ans