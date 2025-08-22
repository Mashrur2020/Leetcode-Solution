# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        def maxget(day, min_price, profit):
            if day >= n:
                return profit
            
            min_price = min(min_price, prices[day])

            profit = max(profit, prices[day] - min_price)
            return maxget(day+1, min_price, profit)

        return maxget(0, float('inf'), 0)