class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low = 0
        high = nums[-1] - nums[0]

        def helperFunction(max_dist: int) -> int:
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > max_dist:
                    left += 1
                count += right - left
            return count
        
        while low < high:
            mid = low + (high - low) // 2
            if helperFunction(mid) >= k:
                high = mid
            else:
                low = mid + 1
        
        return low
        
