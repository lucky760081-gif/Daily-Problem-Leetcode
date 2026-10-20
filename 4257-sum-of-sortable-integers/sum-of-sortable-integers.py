class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        target = sorted(nums)
        ans = 0

        def is_rotation(a, b):
            k = len(a)
            if a == b:
                return True

            pattern = a
            pi = [0] * k
            j = 0

            for i in range(1, k):
                while j and pattern[i] != pattern[j]:
                    j = pi[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                pi[i] = j

            j = 0
            for x in b + b[:-1]:
                while j and x != pattern[j]:
                    j = pi[j - 1]
                if x == pattern[j]:
                    j += 1
                if j == k:
                    return True

            return False

        for k in range(1, n + 1):
            if n % k:
                continue

            valid = True

            for start in range(0, n, k):
                if not is_rotation(nums[start:start + k], target[start:start + k]):
                    valid = False
                    break

            if valid:
                ans += k

        return ans
