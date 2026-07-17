class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        cnt = [0] * (mx + 1)
        for g in range(1, mx + 1):
            for j in range(g, mx + 1, g):
                cnt[g] += freq[j]

        pairs = [0] * (mx + 1)
        for g in range(mx, 0, -1):
            c = cnt[g]
            pairs[g] = c * (c - 1) // 2
            for j in range(g * 2, mx + 1, g):
                pairs[g] -= pairs[j]

        pref = []
        vals = []
        s = 0
        for g in range(1, mx + 1):
            if pairs[g]:
                s += pairs[g]
                pref.append(s)
                vals.append(g)

        ans = []
        for q in queries:
            ans.append(vals[bisect_left(pref, q + 1)])

        return ans