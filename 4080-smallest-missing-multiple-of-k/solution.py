class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        n = 1

        while i < len(nums):
            if k*n < nums[i]:
                return k*n
            if k*n == nums[i]:
                n += 1
            i += 1
        
        return k*n
