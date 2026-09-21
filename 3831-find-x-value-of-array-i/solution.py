class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res = [0] * k
        dp = [0] * k

        for num in nums:
            val = num % k
            next_dp = [0] * k
            next_dp[val] += 1

            for r in range(k):
                if dp[r] > 0:
                    new_rem = (r * val) % k
                    next_dp[new_rem] += dp[r]

            for r in range(k):
                res[r] += next_dp[r]
            
            dp = next_dp
        
        return res
