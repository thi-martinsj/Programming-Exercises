class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        value_to_buy = prices[0]
        n = len(prices)

        for i in range(1, n):
            if prices[i] <= value_to_buy:
                value_to_buy = prices[i]
                continue

            value = prices[i] - value_to_buy
            max_profit += max(value, 0)
            value_to_buy = prices[i]
        
        return max_profit