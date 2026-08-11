class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = nums[0]
        i = 1
        while i < n and nums[i] == nums[i-1] + 1:
            prefix_sum += nums[i]
            i += 1

        num_set = set(nums)
        
        while prefix_sum in num_set:
            prefix_sum += 1
        
        return prefix_sum
