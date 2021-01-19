class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int],
                                 r: list[int]) -> list[bool]:
        # simply add the results of validations for each subarray
        return [
            self.validate(nums[left:right + 1]) for left, right in zip(l, r)
        ]

    # helper method to validate subsequence
    def validate(self, nums: list[int]) -> bool:
        # get set of nums
        st = set(nums)
        # validate uniques (only valid subsequence if 1 unique num)
        if len(st) != len(nums): return len(st) == 1
        # get min/max of nums
        mn, mx = min(nums), max(nums)
        # verify valid from start to finish
        if (mx - mn) % (len(nums) - 1) != 0: return False
        # calculate step (diff between nums)
        step = (mx - mn) // (len(nums) - 1)
        # build arithmetic sequence artifially
        for i in range(mn, mx, step):
            # check if this number is in our set (o(1) lookup)
            if i not in st:
                return False
        # no probs
        return True