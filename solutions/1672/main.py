class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # max wealth so far
        maxWealth = float('-inf')

        # iterate through each person
        for account in accounts:
            # current sum of this person's accounts
            curSum = 0

            # iterate thru individual balances
            for balance in account:
                curSum += balance

            # set new max wealth 
            maxWealth = max(maxWealth, curSum)

        return maxWealth