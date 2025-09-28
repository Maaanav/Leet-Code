class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = [""]
        for c in s:
            temp = []
            if c.isalpha():
                for o in res:
                    temp.append(o+c.upper())
                    temp.append(o+c.lower())
            else:
                for o in res:
                    temp.append(o+c)
            res = temp
        return res
        
