class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [x * x for x in nums]
        nums.sort()

        res = 0
        n = len(nums) // 2

        for i, x in enumerate(nums):
            res += -x if i < n else x
        
        return res
