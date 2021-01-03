class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # count of each individual nums (nums can only be [0, 100])
        counts = [0] * 101
        # smaller than
        smallerThan = [0] * 101
        # fill counts
        for num in nums: counts[num] += 1
        # add running sum of previous number (full count of all nums smaller than)
        # in smallerThan array
        for i in range(1, len(smallerThan)):
            smallerThan[i] += counts[i-1] + smallerThan[i-1]

        # return map of nums, where each num is its smallerThan amount
        return map(lambda x: smallerThan[x], nums)