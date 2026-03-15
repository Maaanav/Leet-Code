class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = -2**31, 2**31-1
        res = 0
        temp = abs(x)

        while temp != 0:
            digit = temp % 10
            res = (res * 10) + digit
            temp //= 10
        
        if x < 0:
            res = -res
        
        if res < MIN or res > MAX:
            return 0
        
        return res
        
