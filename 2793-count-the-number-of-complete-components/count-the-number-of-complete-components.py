class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        vis = [False] * n
        ans = 0

        for i in range(n):
            if vis[i]:
                continue

            stack = [i]
            vis[i] = True
            comp = []

            while stack:
                u = stack.pop()
                comp.append(u)
                for v in graph[u]:
                    if not vis[v]:
                        vis[v] = True
                        stack.append(v)

            sz = len(comp)
            ok = True
            for u in comp:
                if len(graph[u]) != sz - 1:
                    ok = False
                    break

            if ok:
                ans += 1

        return ans