class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max profit and current minimum price
        maxProfit, curMin = 0, float('inf')

        for price in prices:
            # compare this price to curmin
            if price < curMin:
                # this is a new curmin
                curMin = price
            else:
                # we can take profit here
                maxProfit = max(maxProfit, price - curMin)

        return maxProfit