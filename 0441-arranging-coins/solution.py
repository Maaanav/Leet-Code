class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        res = 0

        while left <= right:
            k = left + (right - left) // 2
            curr = k * (k + 1) // 2

            if curr <= n:
                res = k
                left = k + 1
            else:
                right = k - 1
            
        return res
        
