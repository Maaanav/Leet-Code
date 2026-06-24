class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for row_num in range(numRows):
            row = [1] * (row_num + 1)
            for j in range(1, row_num):
                row[j] = res[row_num-1][j-1] + res[row_num-1][j]
            res.append(row)
        return res
