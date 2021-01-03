class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # result
        res = 0
        # counts of each num (nums can only be 0 - 100)
        counts = [0] * 101

        # go through each num
        for num in nums:
            # add to res the amount of nums thats in counts (j > i here, and those are identical nums)
            res += counts[num]
            # increment counts
            counts[num] += 1

        return res