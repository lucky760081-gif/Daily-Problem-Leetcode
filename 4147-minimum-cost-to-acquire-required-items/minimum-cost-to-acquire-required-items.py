class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        ans =  min(need1 * cost1 + need2 * cost2, max(need1, need2) * costBoth, min(need1, need2) * costBoth + max(0, need1 - need2) * cost1 + max(0, need2 - need1) * cost2)
        return ans