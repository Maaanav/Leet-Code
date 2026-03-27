class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gastot = 0
        costtot = 0

        for i in range(len(gas)):
            gastot = gastot + gas[i]
            costtot = costtot + cost[i]

        if gastot < costtot:
            return -1  

        res = 0
        tank = 0
        for i in range(0,len(gas)):

            tank += gas[i]  - cost[i]

            if tank < 0:
                res = i+1
                tank = 0
        
        return res

