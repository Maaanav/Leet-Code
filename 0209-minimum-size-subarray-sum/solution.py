class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        res = float('inf')
        total = 0

        for i in range(len(nums)):
            total += nums[i]

            while total >= target:
                res = min(res, i-left+1)
                total -= nums[left]
                left += 1

        if res == float('inf'):
            return 0
        else:
            return res



        
