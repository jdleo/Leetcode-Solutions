class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # number of balanced strings, and current balance
        res = bal = 0

        # iterate thru string
        for char in s:
            # subtract balance if L, add if R
            bal += 1 if char == "R" else -1
            # check if balanced, if so increment res
            if bal == 0:
                res += 1

        return res