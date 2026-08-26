class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ones = []
        
        for i, ch in enumerate(s):
            if ch == '1':
                ones.append(i)

        if len(ones) < k:
            return ""

        best_len = len(s) + 1
        ans = ""

        for i in range(len(ones) - k + 1):
            l = ones[i]
            r = ones[i + k - 1]

            length = r - l + 1

            if length < best_len:
                best_len = length
                ans = s[l:r + 1]
            elif length == best_len:
                cur = s[l:r + 1]
                if cur < ans:
                    ans = cur

        return ans