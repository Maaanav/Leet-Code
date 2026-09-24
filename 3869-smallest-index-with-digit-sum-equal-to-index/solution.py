class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            digit = nums[i]
            sum_digit = 0
            while digit:
                sum_digit += digit % 10
                digit = digit // 10
            
            if sum_digit == i:
                return i
            
            i += 1
        
        return -1
