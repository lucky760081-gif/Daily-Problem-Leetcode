class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        count = {}

        for i in range(n - k + 1):
            seen = set(nums[i:i + k])

            for x in seen:
                count[x] = count.get(x, 0) + 1

        ans = -1

        for x, c in count.items():
            if c == 1:
                ans = max(ans, x)

        return ans
        