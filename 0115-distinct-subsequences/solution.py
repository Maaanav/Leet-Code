class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(t)
        dp = [0] * (n+1)
        dp[n] = 1

        for char_s in reversed(s):
            for j in range(n):
                if char_s == t[j]:
                    dp[j] += dp[j+1]
        
        return dp[0]
