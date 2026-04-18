class Solution:
    def checkString(self, s: str) -> bool:
        b_flag = False

        for n in s:
            if n == 'b':
                b_flag = True
            if n == 'a' and b_flag:
                return False
        
        return True
        
