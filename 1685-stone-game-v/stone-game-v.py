class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        n = len(stoneValue)
        if n <= 1:
            return 0
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
        
        def get_sum(l, r):
            return prefix[r + 1] - prefix[l]
        
        dp = [[0] * n for _ in range(n)]
        left_max = [[0] * n for _ in range(n)]
        right_max = [[0] * n for _ in range(n)]
        
        for i in range(n):
            left_max[i][i] = stoneValue[i]
            right_max[i][i] = stoneValue[i]
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Binary search largest k in [i, j-1] with sum(i..k) <= sum(k+1..j)
                lo, hi = i, j - 1
                mid = i - 1
                while lo <= hi:
                    m = (lo + hi) // 2
                    if get_sum(i, m) <= get_sum(m + 1, j):
                        mid = m
                        lo = m + 1
                    else:
                        hi = m - 1
                
                best = 0
                
                # k = i to mid: left <= right  --> use left_max[i][mid]
                if mid >= i:
                    best = max(best, left_max[i][mid])
                    # equal case (at most one because values > 0)
                    if get_sum(i, mid) == get_sum(mid + 1, j):
                        best = max(best, get_sum(i, mid) + dp[mid + 1][j])
                
                # k = mid+1 to j-1: left > right --> m = k+1 from mid+2 to j
                if mid + 1 <= j - 1:
                    start_m = mid + 2
                    best = max(best, right_max[start_m][j])
                
                dp[i][j] = best
            
            # Update the max arrays for this length
            for i in range(n - length + 1):
                j = i + length - 1
                s = get_sum(i, j)
                left_max[i][j] = max(left_max[i][j - 1], s + dp[i][j])
                right_max[i][j] = max(right_max[i + 1][j], s + dp[i][j])
        
        return dp[0][n - 1]