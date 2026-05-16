class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]

        for p in prices:
            profit = p - min_buy
            max_profit = max(profit, max_profit)
            min_buy = min(p, min_buy)

        return max_profit