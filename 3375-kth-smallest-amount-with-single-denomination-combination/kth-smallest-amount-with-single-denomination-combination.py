class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        coins = list(set(coins))
        m = len(coins)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return a // gcd(a, b) * b

        subsets = []

        for mask in range(1, 1 << m):
            x = 1
            bits = 0
            valid = True

            for i in range(m):
                if mask & (1 << i):
                    bits += 1
                    x = lcm(x, coins[i])

                    if x > 10**18:
                        valid = False
                        break

            if valid:
                subsets.append((x, bits))

        def count(x):
            total = 0

            for d, bits in subsets:
                if bits & 1:
                    total += x // d
                else:
                    total -= x // d

            return total

        lo = 1
        hi = min(coins) * k

        while lo < hi:
            mid = (lo + hi) // 2

            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo