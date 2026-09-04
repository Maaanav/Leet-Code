class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        
        suf_min = [0] * n
        suf_min[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suf_min[i] = min(suf_min[i+1], nums[i])
 
        res = float('-inf')

        for i in range(n):
            res = max(res, nums[i])
            if res - suf_min[i] <= k:
                return i

        return -1 
