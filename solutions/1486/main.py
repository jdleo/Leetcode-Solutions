class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # res and pointer for odd nums
        res = i = 0

        # go n times
        while i < n:
            # xor res with the i'th odd number from start
            res ^= (start + 2 * i)
            i += 1

        return res