class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        first = [n] * 26
        last = [-1] * 26

        for i, c in enumerate(s):
            x = ord(c) - 97
            first[x] = min(first[x], i)
            last[x] = i

        intervals = []

        for x in range(26):
            if first[x] == n:
                continue

            l = first[x]
            r = last[x]
            i = l
            valid = True

            while i <= r:
                y = ord(s[i]) - 97

                if first[y] < l:
                    valid = False
                    break

                r = max(r, last[y])
                i += 1

            if valid:
                intervals.append((r, l))

        intervals.sort()

        ans = []
        end = -1

        for r, l in intervals:
            if l > end:
                ans.append(s[l:r + 1])
                end = r

        return ans