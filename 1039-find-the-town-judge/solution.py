class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        score = [0] * (n+1)

        for p, t in trust:
            score[p] -= 1
            score[t] += 1

        for i in range(1, n+1):
            if score[i] == n-1:
                return i

        return -1 
        
