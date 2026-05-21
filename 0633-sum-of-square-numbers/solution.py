class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        left = 0
        right = int(math.isqrt(c))

        while left <= right:
            ans = left * left + right * right
            if c == ans:
                return True
            elif ans > c:
                right -= 1
            else:
                left += 1
            
        return False

        
