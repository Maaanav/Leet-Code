class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        target = total_sum // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for stone in stones:
            for w in range(target, stone - 1, -1):
                if dp[w - stone]:
                    dp[w] = True
        
        for w in range(target,-1, -1):
            if dp[w]:
                closest_sum = w
                break
        
        return total_sum - 2 * closest_sum
