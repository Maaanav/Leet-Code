class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])
        res = 0

        is_sorted = [False] * (rows-1)

        for j in range(cols):
            is_bad = False
            for i in range(rows-1):
                if not is_sorted[i] and strs[i][j] > strs[i+1][j]:
                    is_bad = True
                    break
            
            if is_bad:
                res += 1
            else:
                for i in range(rows - 1):
                    if strs[i][j] < strs[i+1][j]:
                        is_sorted[i] = True
        
        return res


        
