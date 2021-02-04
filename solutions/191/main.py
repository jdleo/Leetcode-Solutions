class Solution:
    def hammingWeight(self, n: int) -> int:
        # total number of 1 bits
        res = 0

        # go until there are no more bits
        while n > 0:
            # only add to res, if rightmost bit is a 1
            res += (n & 1)
            # right shift n
            n >>= 1

        return res