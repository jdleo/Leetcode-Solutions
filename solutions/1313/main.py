class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        # result array
        res = []

        # go through nums
        for i in range(len(nums)//2):
            # get freq, val
            freq, val = nums[i*2], nums[i*2 + 1]
            # add val freq times to res
            res.extend([val] * freq)

        return res