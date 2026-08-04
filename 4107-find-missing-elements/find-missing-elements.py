class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set(nums)
        mn = min(nums)
        mx = max(nums)

        ans = []
        for x in range(mn + 1, mx):
            if x not in s:
                ans.append(x)

        return ans