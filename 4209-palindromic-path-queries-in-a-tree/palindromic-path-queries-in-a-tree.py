class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type s: str
        :type queries: List[str]
        :rtype: List[bool]
        """
        from collections import defaultdict

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0
        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()
            if state == 0:
                parent[u] = p
                tin[u] = timer
                timer += 1
                stack.append((u, p, 1))
                for v in reversed(adj[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        LOG = n.bit_length()
        up = [parent[:]]
        for j in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] if prev[i] != -1 else -1 for i in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit = 0
            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        bit = [0] * (n + 1)

        def add(i, val):
            i += 1
            while i <= n:
                bit[i] ^= val
                i += i & -i

        def pref(i):
            res = 0
            i += 1
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res

        chars = [ord(c) - 97 for c in s]

        for u in range(n):
            add(tin[u], 1 << chars[u])
            add(tout[u], 1 << chars[u])

        ans = []

        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = ord(parts[2]) - 97
                if chars[u] != c:
                    val = (1 << chars[u]) ^ (1 << c)
                    add(tin[u], val)
                    add(tout[u], val)
                    chars[u] = c
            else:
                u = int(parts[1])
                v = int(parts[2])
                w = lca(u, v)

                mask = pref(tin[u]) ^ pref(tin[v]) ^ (1 << chars[w])
                ans.append(mask & (mask - 1) == 0)

        return ans