class Solution:
    def maxSumOfSquares(self, num: int, sum_val: int) -> str:
        if sum_val > 9 * num:
            return ""
        
        nines = sum_val // 9
        rem = sum_val % 9

        res = []

        for _ in range(nines):
            res.append("9")
        
        if rem > 0:
            res.append(str(rem))
        
        while len(res) < num:
            res.append("0")
        
        return "".join(res)
