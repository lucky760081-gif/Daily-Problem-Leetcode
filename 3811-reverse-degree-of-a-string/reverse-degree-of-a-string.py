class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0

        for i, ch in enumerate(s, 1):
            value = 26 - (ord(ch) - ord('a'))
            ans += value * i

        return ans