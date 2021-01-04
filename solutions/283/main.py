class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # distance from current number to first zero
        dist = 0

        # go thru nums
        for i in range(len(nums)):
            # check if zero
            if nums[i] == 0:
                # increase distance
                dist += 1
            elif dist > 0:
                # swap current number with first zero
                nums[i - dist] = nums[i]
                nums[i] = 0