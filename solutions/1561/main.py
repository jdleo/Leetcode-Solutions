class Solution:
    '''
    explanation of solution:
    suppose we start with [2,4,1,2,7,8]
    sorting desc gives us [8,7,4,2,2,1]
    alice will of course pick 8, so we need to pick 7, bob picks 4
    we now have 2,2,1
    alice of course picks 2, we pick 2, bob picks 1
    '''
    def maxCoins(self, piles: List[int]) -> int:
        # result coins and index for loop
        res, index = 0, 1

        # sort pile descending to have clear view of maximums
        piles.sort(reverse=True)

        while index < len(piles):
            # always take 2nd pile
            res += piles[index]
            # always remove last pile
            piles.pop()
            # move to next group of 3
            index += 2

        return res