class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        h = n // 2

        left = right = 0
        ql = qr = 0

        for i in range(h):
            if num[i] == '?':
                ql += 1
            else:
                left += int(num[i])

        for i in range(h, n):
            if num[i] == '?':
                qr += 1
            else:
                right += int(num[i])

        if (ql + qr) % 2:
            return True

        return 2 * (left - right) != 9 * (qr - ql)