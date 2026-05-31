class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = 0
        temp = 0

        while numBottles > 0 or temp >= numExchange:
            if numBottles > 0:
                res += numBottles
                temp += numBottles
                numBottles = 0
            
            if temp >= numExchange:
                temp -= numExchange
                numBottles += 1
                numExchange += 1
                
        return res 
