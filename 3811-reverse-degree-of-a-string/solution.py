class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        count = 1
        for c in s:
            intvalue = ord('z') - ord(c) + 1
            intvalue *= count
            res += intvalue 
            count += 1
        
        return res
