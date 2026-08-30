class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        min_idx = 0
        max_idx = 0
        for i in range(1,n):
            if nums[i] < nums[min_idx]:
                min_idx = i
            if nums[i] > nums[max_idx]:
                max_idx = i
        
        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        return min(right + 1,  n - left, (left + 1) + (n - right))
