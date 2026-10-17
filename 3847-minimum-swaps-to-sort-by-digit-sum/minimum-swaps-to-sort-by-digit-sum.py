class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        n = len(nums)
        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {v: i for i, v in enumerate(nums)}
        visited = [False] * n
        ans = 0

        for i in range(n):
            if visited[i] or pos[sorted_nums[i]] == i:
                visited[i] = True
                continue

            cycle = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = pos[sorted_nums[j]]
                cycle += 1

            ans += cycle - 1

        return ans
