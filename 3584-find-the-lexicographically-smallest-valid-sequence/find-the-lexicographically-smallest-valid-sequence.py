class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        n, m = len(word1), len(word2)

        right = [-1] * m
        p = n - 1

        for j in range(m - 1, -1, -1):
            while p >= 0 and word1[p] != word2[j]:
                p -= 1
            if p >= 0:
                right[j] = p
                p -= 1

        ans = []
        i = 0
        used = False

        for j in range(m):
            while i < n:
                if word1[i] == word2[j]:
                    ans.append(i)
                    i += 1
                    break

                if (not used) and (
                    j == m - 1 or (right[j + 1] != -1 and right[j + 1] > i)
                ):
                    used = True
                    ans.append(i)
                    i += 1
                    break

                i += 1
            else:
                return []

        return ans