class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opened = 0
        ans = []
        for n in s:
            if n == '(':
                if opened > 0:
                    ans.append(n)
                opened += 1
            if n == ')':
                if opened > 1:
                    ans.append(n)
                opened -= 1
        
        return "".join(ans)
        
