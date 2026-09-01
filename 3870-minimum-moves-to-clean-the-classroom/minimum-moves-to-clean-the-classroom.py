class Solution(object):
    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """
        m = len(classroom)
        n = len(classroom[0])

        litter_id = {}
        start = -1
        k = 0

        for i in range(m):
            for j in range(n):
                ch = classroom[i][j]
                pos = i * n + j

                if ch == 'S':
                    start = pos
                elif ch == 'L':
                    litter_id[pos] = k
                    k += 1

        if k == 0:
            return 0

        target = (1 << k) - 1
        size = m * n
        grid = ''.join(classroom)

        best = [[-1] * size for _ in range(1 << k)]
        best[0][start] = energy

        q = deque([(start, energy, 0)])
        moves = 0

        while q:
            for _ in range(len(q)):
                pos, e, mask = q.popleft()

                if mask == target:
                    return moves

                x = pos // n
                y = pos % n

                neighbors = []

                if x > 0:
                    neighbors.append(pos - n)
                if x + 1 < m:
                    neighbors.append(pos + n)
                if y > 0:
                    neighbors.append(pos - 1)
                if y + 1 < n:
                    neighbors.append(pos + 1)

                for np in neighbors:
                    ch = grid[np]

                    if ch == 'X':
                        continue

                    ne = e - 1

                    if ne < 0:
                        continue

                    nmask = mask

                    if np in litter_id:
                        nmask |= 1 << litter_id[np]

                    if ch == 'R':
                        ne = energy

                    if ne <= best[nmask][np]:
                        continue

                    best[nmask][np] = ne
                    q.append((np, ne, nmask))

            moves += 1

        return -1