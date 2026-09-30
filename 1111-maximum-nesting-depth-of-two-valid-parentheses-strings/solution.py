class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = []
        depth = 0
        i = 0
        for char in seq:
            if char == '(':
                depth += 1
                if depth % 2 == 0:
                    res.append(0) 
                else:
                    res.append(1)
            else:
                if depth % 2 == 0:
                    res.append(0)
                else:
                    res.append(1)
                depth -= 1
        
        return res
