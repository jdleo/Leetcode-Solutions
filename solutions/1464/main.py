class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # to hold first and second biggest numbers
        # note: nums are bound in [1, 10^3]
        first = second = 0

        # go thru nums
        for num in nums:
            # check if this is max
            if num > first:
                # move first to second, and num to first
                first, second = num, first
            else:
                # set second as normal
                second = max(second, num)

        # we have two biggest nums, so just return what they want
        return (first - 1) * (second - 1)