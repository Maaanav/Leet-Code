class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cost = 0
        openb = 0
        for char in s:
            if char == '(':
                openb += 1
            else:
                if openb > 0:
                    openb -= 1
                else:
                    cost += 1
        
        return cost + openb
