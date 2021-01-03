class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # go from 1 to length of array
        for i in range(1, len(nums)):
            # keep adding from the last number to get a running sum
            nums[i] += nums[i-1]

        return nums