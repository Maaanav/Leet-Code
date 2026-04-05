class Solution:
    def judgeCircle(self, moves: str) -> bool:
        res = [0,0,0,0]

        for i in moves:
            if i  == 'L':
                res[0] = res[0]+1
            elif i == 'R':
                res[1] = res[1]+1
            elif i == 'U':
                res[2] = res[2]+1
            else:
                res[3] = res[3]+1
        
        ans1 = res[0] - res[1]
        ans2 = res[2] - res[3]

        return ans1 == 0 and ans2 == 0

        
