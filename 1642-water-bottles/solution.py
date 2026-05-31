class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        temp = 0

        while(numBottles> 0):
            res += numBottles
            temp += numBottles
            numBottles = temp // numExchange
            temp = temp % numExchange

        return res
