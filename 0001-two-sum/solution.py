class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_table = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in dict_table:
                return [dict_table[diff], i]
            dict_table[num] = i
        
        return 

