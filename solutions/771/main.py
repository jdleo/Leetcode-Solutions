class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # number of stones that are jewels
        res = 0
        # make jewels a set of chars, for o(1) lookups
        jewels = set(jewels)

        # go thru stones
        for stone in stones:
            # check if this stone is a jewel
            if stone in jewels: res += 1
        
        return res