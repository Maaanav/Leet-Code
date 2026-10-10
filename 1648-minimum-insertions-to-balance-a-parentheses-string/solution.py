class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        i = 0
        count = 0
        res = 0
        while (i < n):
            if s[i] == '(':
                count += 1
                i += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    res += 1
                
                if i+1 < n and s[i+1] == ')':
                    i += 2
                else:
                    res += 1
                    i += 1
                
        return res + (count * 2)
            

