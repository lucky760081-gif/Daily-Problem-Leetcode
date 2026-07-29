class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        LIMIT = 10**6 + 1

        freq = Counter(s)

        mid = ""
        half = [0] * 26

        for ch, cnt in freq.items():
            if cnt & 1:
                mid = ch
            half[ord(ch) - 97] = cnt // 2

        def count_perm(cnts):
            total = sum(cnts)
            res = 1
            rem = total

            for c in cnts:
                if c:
                    res *= comb(rem, c)
                    if res >= LIMIT:
                        return LIMIT
                    rem -= c

            return res

        total_perm = count_perm(half)
        if total_perm < k:
            return ""

        left = []
        m = sum(half)

        for _ in range(m):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                ways = count_perm(half)

                if ways >= k:
                    left.append(chr(i + 97))
                    break

                k -= ways
                half[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]