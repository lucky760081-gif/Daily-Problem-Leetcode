class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 0
        s = 0

        for ch in str(n):
            if ch != '0':
                d = int(ch)
                x = x * 10 + d
                s += d

        return x * s