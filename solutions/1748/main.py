class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        # array to hold count for each num 1 <= nums[i] <= 100
        counts = [0] * 101
        # fill counts
        for num in nums: counts[num] += 1
        # result (sum of uniques)
        res = 0
        # go thru counts
        for i in range(len(counts)):
            # if this is a unique number, add number to res
            if counts[i] == 1: res += i
        return res