class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        s = "123456789"
        ans = []

        for l in range(2, 10):
            for i in range(10 - l):
                x = int(s[i:i + l])
                if low <= x <= high:
                    ans.append(x)

        return ans