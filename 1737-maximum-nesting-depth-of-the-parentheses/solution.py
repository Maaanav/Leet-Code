class Solution:
    def maxDepth(self, s: str) -> int:
        
        res = 0
        curr = 0
        for char in s:
            if char == '(':
                curr += 1
                res = max(curr, res)
            elif char == ')':
                curr -= 1
        
        return res
