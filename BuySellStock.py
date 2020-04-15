class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Take a pass to find the min buying price 
        # Check all subsequent selling pricce against the min buy value
        # return the max profit
        max_profit = 0
        min_price = float('Inf')
        for p in prices:
            if p < min_price: min_price = p
            curr_profit = p - min_price
            max_profit = max(max_profit, curr_profit)
        return max_profit
