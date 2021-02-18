class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        # we know the first num
        res = [first]

        # go thru nums in encoded arr
        for num in encoded:
            # add current number xor'd with last number in res
            res.append(num ^ res[-1])

        return res