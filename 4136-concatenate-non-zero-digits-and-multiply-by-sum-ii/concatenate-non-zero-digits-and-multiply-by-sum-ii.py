class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        n = len(s)

        # powers of 10
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # prefix count of non-zero digits
        cnt = [0] * (n + 1)

        # prefix sum of non-zero digits
        sm = [0] * (n + 1)

        # prefix concatenated value of non-zero digits
        val = [0] * (n + 1)

        for i in range(n):
            d = ord(s[i]) - ord('0')
            cnt[i + 1] = cnt[i]
            sm[i + 1] = sm[i]
            val[i + 1] = val[i]

            if d:
                cnt[i + 1] += 1
                sm[i + 1] += d
                val[i + 1] = (val[i] * 10 + d) % MOD

        ans = []

        for l, r in queries:
            c = cnt[r + 1] - cnt[l]
            x = (val[r + 1] - val[l] * pow10[c]) % MOD
            ssum = sm[r + 1] - sm[l]
            ans.append((x * ssum) % MOD)

        return ans