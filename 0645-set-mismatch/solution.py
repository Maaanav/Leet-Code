class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = -1
        m = -1

        for n in nums:
            val = abs(n)
            if nums[val-1] < 0:
                d = val
            else:
                nums[val - 1] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                m = i+1
        
        return [d,m]

        
