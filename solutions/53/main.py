class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maximum sub array sum (first number by default)
        res = nums[0]

        # go thru nums
        for i in range(1, len(nums)):
            # we can either continue the subarray, or start new subarray
            nums[i] = max(nums[i - 1] + nums[i], nums[i])
            # set new max
            res = max(res, nums[i])

        return res