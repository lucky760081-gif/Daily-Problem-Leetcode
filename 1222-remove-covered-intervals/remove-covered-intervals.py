class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))

        ans = 0
        end = 0

        for _, r in intervals:
            if r > end:
                ans += 1
                end = r

        return ans