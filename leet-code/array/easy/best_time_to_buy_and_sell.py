class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        value_to_buy = prices[0]
        max_profit = 0
        n = len(prices)

        for i in range(1, n):
            if prices[i] < value_to_buy:
                value_to_buy = prices[i]
            
            if (prices[i] - value_to_buy) > max_profit:
                max_profit = prices[i] - value_to_buy
        
        return max_profit
