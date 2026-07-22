class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        ones = s.count('1')

        if '0' in s:
            blocks = [(m.start(), m.end() - 1) for m in re.finditer(r'0+', s)]
            zs = [x for x, _ in blocks]
            ze = [y for _, y in blocks]
        else:
            zs, ze = [], []

        nblocks = len(zs)

        lengths = [ze[i] - zs[i] + 1 for i in range(nblocks)]
        V = [a + b for a, b in pairwise(lengths)]

        nv = len(V)
        sparse = [V]
        half = 1
        while half * 2 <= nv:
            prev = sparse[-1]
            sparse.append([max(prev[i], prev[i + half]) for i in range(len(prev) - half)])
            half *= 2

        def rmq(lo: int, hi: int) -> int:
            if lo > hi:
                return 0
            t = (hi - lo + 1).bit_length() - 1
            return max(sparse[t][lo], sparse[t][hi - (1 << t) + 1])

        def clip(j: int, l: int, r: int) -> int:
            return (
                V[j]
                - max(0, l - zs[j])
                - max(0, ze[j + 1] - r)
            )

        ans = []

        for l, r in queries:
            if nblocks < 2:
                ans.append(ones)
                continue

            ja = bisect_left(ze, l)
            jb = bisect_right(zs, r) - 2

            if ja > jb:
                ans.append(ones)
                continue

            best = max(
                clip(ja, l, r),
                clip(jb, l, r),
                rmq(ja + 1, jb - 1) if jb - ja >= 2 else 0,
            )

            ans.append(ones + best)

        return ans