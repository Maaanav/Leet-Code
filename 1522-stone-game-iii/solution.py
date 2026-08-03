class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp1 = dp2 = dp3 = 0

        for i in range(n-1, -1, -1):
            max_diff = float('-inf')
            curr_sum = 0
            for x in range(1,4):
                if i + x - 1 < n:
                    curr_sum += stoneValue[i + x - 1]
                    next_dp = dp1 if x == 1 else (dp2 if x == 2 else dp3)
                    max_diff = max(max_diff, curr_sum - next_dp)
            
            dp3 = dp2
            dp2 = dp1
            dp1 = max_diff
        
        return "Alice" if dp1 > 0 else ("Bob" if dp1 < 0 else "Tie")
