class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # current minimum stock price, and total profit
        curMin, profit = float('inf'), 0

        # iter thru prices
        for price in prices:
            # check if we can take a profit (sell)
            if price > curMin:
                # sell stock and set curMin to this price
                profit += price - curMin
                curMin = price
            else:
                # set new min
                curMin = price

        return profit