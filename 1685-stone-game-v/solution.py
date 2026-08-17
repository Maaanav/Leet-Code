class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        if n <= 1:
            return 0

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]

        def get_sum(l: int, r: int) -> int:
            return pref[r + 1] - pref[l]

        dp = [[0] * n for _ in range(n)]
        L = [[0] * n for _ in range(n)]
        R = [[0] * n for _ in range(n)]

        for i in range(n):
            L[i][i] = stoneValue[i]  
            R[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            mid = 0 
            for i in range(n - length + 1):
                j = i + length - 1

                if mid < i:
                    mid = i
                while mid < j - 1 and get_sum(i, mid + 1) * 2 <= get_sum(i, j):
                    mid += 1

                res = L[i][mid] if get_sum(i, mid) * 2 < get_sum(i, j) else 0

                left_split = mid + 1 if get_sum(i, mid) * 2 < get_sum(i, j) else mid
                if left_split < j:
                    res = max(res, R[left_split + 1][j])

                if get_sum(i, mid) * 2 == get_sum(i, j):
                    res = max(res, L[i][mid], R[mid + 1][j])

                dp[i][j] = res

                L[i][j] = max(L[i][j - 1], get_sum(i, j) + dp[i][j])
                R[i][j] = max(R[i + 1][j], get_sum(i, j) + dp[i][j])

        return dp[0][n - 1]
