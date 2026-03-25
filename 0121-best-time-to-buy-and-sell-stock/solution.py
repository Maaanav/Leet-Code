class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_p = 0

        for p in prices:
            if p < min_price:
                min_price = p
            
            curr_p = p - min_price

            if curr_p > max_p:
                max_p = curr_p
        
        return max_p
        

        
