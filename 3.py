class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        memo = [[[-1]*(k+1) for i in range(2)] for i in range(n)]

        def getmax(day, stock, count):
            if day >= n:
                return 0

            if count == k:
                return 0
            
            if memo[day][stock][count] != -1:
                return memo[day][stock][count]

            if stock == 1:
                # sell/hold
                sell = prices[day] + getmax(day+1, 0, count+1)
                hold = getmax(day+1, 1, count)

                profit = max(sell, hold)
                memo[day][stock][count] = profit
                return profit
            else:
                #buy/skio
                buy = -prices[day] + getmax(day+1, 1, count)
                skip = getmax(day+1, 0, count)

                profit = max(buy, skip)
                memo[day][stock][count] = profit

                return profit

        return getmax(0, 0, 0)