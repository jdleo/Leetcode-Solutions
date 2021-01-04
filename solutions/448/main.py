class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # iterate thru nums
        for i in range(len(nums)):
            # get index 0-indexed
            index = abs(nums[i]) - 1
            # mark this num as visited
            nums[index] = -abs(nums[index])

        # return the numbers 1 to n that have NOT been visited
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]