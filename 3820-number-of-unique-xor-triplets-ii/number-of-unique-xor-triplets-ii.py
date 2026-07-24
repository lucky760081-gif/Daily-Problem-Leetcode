class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MAXX = 2048  # nums[i] <= 1500 < 2^11

        pair = [False] * MAXX
        for a in nums:
            for b in nums:
                pair[a ^ b] = True

        ans = [False] * MAXX
        for x in range(MAXX):
            if pair[x]:
                for v in nums:
                    ans[x ^ v] = True

        return sum(ans)