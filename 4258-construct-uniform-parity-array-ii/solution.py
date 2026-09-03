class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')
        for num in nums1:
            if num % 2 != 0:
                min_odd = min(min_odd, num)
        
        if min_odd == float('inf'):
            return True
        
        for num in nums1:
            if num % 2 == 0 and num < min_odd:
                return False
        
        return True
