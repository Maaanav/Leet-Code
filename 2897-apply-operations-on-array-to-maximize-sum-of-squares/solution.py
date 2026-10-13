class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        count = [0] * 31
        for x in nums:
            for i in range(31):
                if (x >> i) & 1:
                    count[i] += 1
        
        res = 0
        for _ in range(k):
            curr = 0
            for i in range(31):
                if count[i] > 0:
                    curr |= 1 << i
                    count[i] -= 1
            res = (res + curr * curr) % MOD 
        
        return res
