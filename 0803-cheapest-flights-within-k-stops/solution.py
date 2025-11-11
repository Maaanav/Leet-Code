class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [float('inf')] * n
        cost[src] = 0

        for stops in range(k+1):
            new_cost = list(cost)

            for u, v, price in flights:
                if cost[u] != inf:
                    new_price = cost[u] + price

                    if new_price < new_cost[v]:
                        new_cost[v] = new_price
            
            cost = new_cost

        result = cost[dst]

        return result if result != inf else -1

        
