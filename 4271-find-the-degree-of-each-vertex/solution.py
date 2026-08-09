class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = [0] * m
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    res[i] += 1
        
        return res
