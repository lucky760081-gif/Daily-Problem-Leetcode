class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        FACTORS = {
            0: {},
            1: {},
            2: {2: 1},
            3: {3: 1},
            4: {2: 2},
            5: {5: 1},
            6: {2: 1, 3: 1},
            7: {7: 1},
            8: {2: 3},
            9: {3: 2},
        }

        def getPrimeCount(x):
            cnt = {2: 0, 3: 0, 5: 0, 7: 0}

            for p in (2, 3, 5, 7):
                while x % p == 0:
                    x //= p
                    cnt[p] += 1

            return cnt, x == 1

        def getPrimeCountFromString(s):
            cnt = {2: 0, 3: 0, 5: 0, 7: 0}

            for ch in s:
                d = ord(ch) - ord('0')
                for p, f in FACTORS[d].items():
                    cnt[p] += f

            return cnt

        def getFactorCount(cnt):
            res = {}

            cnt8 = cnt[2] // 3
            rem2 = cnt[2] % 3

            cnt9 = cnt[3] // 2
            cnt3 = cnt[3] % 2

            cnt4 = rem2 // 2
            cnt2 = rem2 % 2

            cnt6 = 0

            if cnt2 == 1 and cnt3 == 1:
                cnt2 = 0
                cnt3 = 0
                cnt6 = 1

            if cnt3 == 1 and cnt4 == 1:
                cnt2 = 1
                cnt6 = 1
                cnt3 = 0
                cnt4 = 0

            res[2] = cnt2
            res[3] = cnt3
            res[4] = cnt4
            res[5] = cnt[5]
            res[6] = cnt6
            res[7] = cnt[7]
            res[8] = cnt8
            res[9] = cnt9

            return res

        def construct(factors):
            ans = []

            for d in range(2, 10):
                ans.append(str(d) * factors.get(d, 0))

            return "".join(ans)

        def isSubset(a, b):
            for k, v in a.items():
                if b.get(k, 0) < v:
                    return False
            return True

        def subtract(a, b):
            res = dict(a)

            for k, v in b.items():
                res[k] = max(0, res.get(k, 0) - v)

            return res

        def sumValues(mp):
            return sum(mp.values())

        primeCount, ok = getPrimeCount(t)

        if not ok:
            return "-1"

        factorCount = getFactorCount(primeCount)

        if sumValues(factorCount) > len(num):
            return construct(factorCount)

        primeCountPrefix = getPrimeCountFromString(num)

        firstZeroIndex = num.find('0')
        if firstZeroIndex == -1:
            firstZeroIndex = len(num)

            if isSubset(primeCount, primeCountPrefix):
                return num

        for i in range(len(num) - 1, -1, -1):
            d = int(num[i])

            primeCountPrefix = subtract(
                primeCountPrefix,
                FACTORS[d]
            )

            spaceAfter = len(num) - 1 - i

            if i > firstZeroIndex:
                continue

            for biggerDigit in range(d + 1, 10):
                need = getFactorCount(
                    subtract(
                        subtract(
                            primeCount,
                            primeCountPrefix
                        ),
                        FACTORS[biggerDigit]
                    )
                )

                if sumValues(need) <= spaceAfter:
                    fillOnes = spaceAfter - sumValues(need)

                    return (
                        num[:i]
                        + str(biggerDigit)
                        + ("1" * fillOnes)
                        + construct(need)
                    )

        need = getFactorCount(primeCount)

        return (
            "1" * (len(num) + 1 - sumValues(need))
            + construct(need)
        )