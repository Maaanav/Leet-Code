class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold = float('-inf')
        held = float('-inf')
        reset = 0

        for price in prices:
            presold = sold

            sold = held + price
            held = max(held, reset - price)
            reset = max(reset, presold)
        
        return max(sold, reset)
