class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # counts for nums
        counts = dict()
        # fill counts (0 as default if not exist)
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # return max of counts with the frequency as key
        return max(counts.keys(), key=counts.get)