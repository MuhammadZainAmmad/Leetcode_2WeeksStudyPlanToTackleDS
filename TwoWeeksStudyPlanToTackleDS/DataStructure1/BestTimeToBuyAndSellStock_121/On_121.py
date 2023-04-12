class Solution(object):
    def maxProfit(self, prices):
        # Solution By ChatGPT

        if len(prices) < 2:
            return 0
        
        smallest_price = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] < smallest_price:
                smallest_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - smallest_price)
                
        return max_profit