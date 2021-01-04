import math


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # number of even digit nums
        res = 0

        # iter thru nums
        for num in nums:
            # check if this num has even digits (log10(n) + 1 is num of digits)
            if math.floor((math.log10(num) + 1) % 2) == 0:
                res += 1

        return res