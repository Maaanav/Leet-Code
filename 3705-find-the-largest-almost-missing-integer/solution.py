class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 1:
            counts = Counter(nums)
            singles = [x for x, freq in counts.items() if freq == 1]
            return max(singles) if singles else -1
        
        if k == n:
            return max(nums)
        
        ans = -1
        if nums.count(nums[0]) == 1:
            ans = max(ans, nums[0])

        if nums.count(nums[-1]) == 1:
            ans = max(ans, nums[-1])
        
        return ans

