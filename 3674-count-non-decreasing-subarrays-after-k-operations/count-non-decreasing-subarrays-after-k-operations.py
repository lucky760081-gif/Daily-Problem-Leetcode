class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        dq = []
        head = 0
        j = n - 1
        cost = 0
        ans = 0

        for i in range(n - 1, -1, -1):
            while len(dq) > head and nums[dq[-1]] < nums[i]:
                l = dq.pop()
                r = dq[-1] if len(dq) > head else j + 1
                cost += (r - l) * (nums[i] - nums[l])

            dq.append(i)

            while cost > k:
                cost -= nums[dq[head]] - nums[j]

                if dq[head] == j:
                    head += 1

                j -= 1

            ans += j - i + 1

        return ans