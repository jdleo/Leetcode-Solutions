class Solution:
    def romanToInt(self, s: str) -> int:
        # mappings for roman values
        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # result number so far, and also last number
        res, last = 0, float('inf')

        # iterate through chars
        for char in s:
            # increment res by roman mapping
            res += romans[char]
            # check if last character was smaller than cur (case IX or IV)
            if last < romans[char]:
                # need to subtract 2*last (case IV would be 6, needs to be 4)
                res -= 2 * last

            last = romans[char]

        return res
