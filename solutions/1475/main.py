class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # stack to hold prices[i]'s
        stack = []
        # go through prices
        for j in range(len(prices)):
            # while stack has values and this price can be used as discount
            while stack and prices[stack[-1]] >= prices[j]:
                # this price can be used as discount, discount item in stack
                prices[stack.pop()] -= prices[j]

            # add price idx to stack
            stack.append(j)

        # return discounted prices
        return prices