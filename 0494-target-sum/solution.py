class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def targetSumWays(index: int, curr_sum: int):
            if index == len(nums):
                return 1 if curr_sum == target else 0
            
            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]

            add_path = targetSumWays(index+1, curr_sum + nums[index])
            sub_path = targetSumWays(index+1, curr_sum - nums[index])

            memo[(index, curr_sum)] = add_path + sub_path
            return memo[(index, curr_sum)]
        
        return targetSumWays(0, 0)
