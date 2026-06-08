class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        
        total_unique = 10
        curr_unique = 9
        a_choices = 9
        
        for i in range(2, n+1):
            curr_unique *= a_choices 
            total_unique += curr_unique
            a_choices -= 1

        return total_unique 

