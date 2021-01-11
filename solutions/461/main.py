class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # total hamming distance
        res = 0

        # go while x or y still has bits left
        while x > 0 or y > 0:
            # xor the rightmost bits to see if they differ
            res += ((x & 1) ^ (y & 1))
            # right shift both
            x >>= 1
            y >>= 1

        return res