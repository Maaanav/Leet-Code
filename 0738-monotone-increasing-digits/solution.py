class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))
        length = len(digits)
        
        m = length

        for i in range(length-1, 0, -1):
            if digits[i-1] > digits[i]:
                digits[i-1] = str(int(digits[i-1]) - 1)
                m = i
        
        for i in range(m, length):
            digits[i] = '9'
        
        return int("".join(digits))
