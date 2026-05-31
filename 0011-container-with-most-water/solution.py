class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        curr, res = 0, 0

        while l < r:
            curr = min(height[l], height[r]) * (r - l)
            res = max(res, curr)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res

