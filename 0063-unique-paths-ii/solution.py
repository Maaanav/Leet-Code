class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        row = [0] * n
        row[0] = 1

        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    row[c] = 0
                elif c > 0:
                    row[c] += row[c - 1] 
        
        return row[-1]
