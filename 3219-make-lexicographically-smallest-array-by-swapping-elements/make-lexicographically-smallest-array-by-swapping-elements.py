class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        n = len(nums)
        pairs = sorted((nums[i], i) for i in range(n))
        ans = nums[:]

        i = 0

        while i < n:
            j = i

            while j + 1 < n and pairs[j + 1][0] - pairs[j][0] <= limit:
                j += 1

            values = sorted(pairs[k][0] for k in range(i, j + 1))
            indices = sorted(pairs[k][1] for k in range(i, j + 1))

            for idx, value in zip(indices, values):
                ans[idx] = value

            i = j + 1

        return ans