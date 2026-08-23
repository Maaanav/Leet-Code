class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        leftsum = 0
        rightsum = 0
        leftquestionmark = 0
        rightquestionmark = 0

        for i in range(n):
            if i < n // 2:
                if num[i] == '?':
                    leftquestionmark += 1
                else:
                    leftsum += int(num[i])
            else:
                if num[i] == '?':
                    rightquestionmark += 1
                else:
                    rightsum += int(num[i])
        
        totalquestionmark = leftquestionmark + rightquestionmark
        
        if totalquestionmark % 2 == 1:
            return True
        
        left = 2 * leftsum + 9 * leftquestionmark
        right = 2 * rightsum + 9 * rightquestionmark

        return left != right
