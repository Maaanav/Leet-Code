class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
            
        vowels = set('aeiouAEIOU')
        flag1 = False
        flag2 = False
        flag3 = False

        for c in word:
            if c.isalpha():
                if c in vowels:
                    flag2 = True
                else:
                    flag3 = True
            elif c.isdigit():
                continue
            else:
                return False
        
        return flag2 and flag3
        
        
