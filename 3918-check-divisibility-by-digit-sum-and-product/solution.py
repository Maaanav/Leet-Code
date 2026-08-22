class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sumdigit = 0
        productdigit = 1
        temp = n
        while temp > 0:
            digit = temp % 10
            sumdigit += digit 
            productdigit *= digit
            temp //= 10
        productdigit += sumdigit
        return n % productdigit == 0
