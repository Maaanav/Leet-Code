class Solution:
    def countCommas(self, n: int) -> int:
        if(n <= 999):
            return 0
        onecomma   = 999999
        twocomma   = 999999999
        threecomma = 999999999999
        fourcomma  = 999999999999999
        fivecomma  = 999999999999999999

        if(999 < n <= onecomma):
            return n - 999
        
        if(onecomma < n <= twocomma):
            return ((n - onecomma) * 2) + (onecomma - 999) 
        
        if(twocomma < n <= threecomma):
            return ((n - twocomma) * 3) + ((twocomma - onecomma) * 2) + (onecomma - 999)
        
        if(threecomma < n <= fourcomma):
            return ((n - threecomma) * 4) + ((threecomma - twocomma) * 3) + ((twocomma - onecomma) * 2) + (onecomma - 999)
        
        return ((n - fourcomma) * 5) + ((fourcomma - threecomma) * 4) + ((threecomma - twocomma) * 3) + ((twocomma - onecomma) * 2) + (onecomma - 999)
