class Solution(object):
    def maximumSaleItems(self, items, budget):
        """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
        n = len(items)
        freq = [0] * (n + 1)

        for factor, price in items:
            freq[factor] += 1

        multiples = [0] * (n + 1)

        for i in range(1, n + 1):
            for j in range(i, n + 1, i):
                multiples[i] += freq[j]

        min_price = min(price for factor, price in items)

        bonus = []
        for factor, price in items:
            count = multiples[factor] - 1
            if count > 0 and price <= 2 * min_price:
                bonus.append((price, count))

        bonus.sort()

        remaining = budget
        ans = 0

        for price, count in bonus:
            take = min(count, remaining // price)
            ans += 2 * take
            remaining -= take * price

        ans += remaining // min_price

        return ans