class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        take = 10
        alice = True
        while n >= take:
            n -= take
            take -= 1
            alice = not alice
        return not alice