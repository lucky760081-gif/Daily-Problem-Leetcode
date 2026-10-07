class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        left = right = 0

        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left:
                    left -= 1
                else:
                    right += 1

        ans = set()

        def dfs(i, path, balance, lrem, rrem):
            if i == len(s):
                if balance == 0 and lrem == 0 and rrem == 0:
                    ans.add(''.join(path))
                return

            ch = s[i]

            if ch == '(':
                if lrem:
                    dfs(i + 1, path, balance, lrem - 1, rrem)

                path.append(ch)
                dfs(i + 1, path, balance + 1, lrem, rrem)
                path.pop()

            elif ch == ')':
                if rrem:
                    dfs(i + 1, path, balance, lrem, rrem - 1)

                if balance > 0:
                    path.append(ch)
                    dfs(i + 1, path, balance - 1, lrem, rrem)
                    path.pop()

            else:
                path.append(ch)
                dfs(i + 1, path, balance, lrem, rrem)
                path.pop()

        dfs(0, [], 0, left, right)
        return list(ans)