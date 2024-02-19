class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0

        max_profit = 0
        min_buy = prices[0]

        for price in prices[1:]:
            max_profit = max(max_profit, price - min_buy)
            min_buy = min(min_buy, price)

        return max_profit
