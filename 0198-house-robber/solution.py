class Solution:
    def rob(self, nums: List[int]) -> int:
        p2, p1 = 0, 0
        for n in nums:
            temp = max(n+p2, p1)
            p2 = p1
            p1 = temp
        
        return temp
        
