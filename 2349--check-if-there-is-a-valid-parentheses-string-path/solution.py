class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m+n-1) % 2 != 0 or grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False

        @lru_cache(None)
        def dp(r: int, c: int, balance: int) -> bool:
            
            if grid[r][c] == '(':
                balance += 1
            else:
                balance -= 1
            
            if balance < 0:
                return False
            
            if r == m-1 and c == n-1:
                return balance == 0

            down = (r+1 < m) and dp(r+1, c, balance)
            right = (c+1 < n) and dp(r, c+1, balance)

            return down or right 

        return dp(0 , 0, 0)
