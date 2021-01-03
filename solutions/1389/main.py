class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        # result array
        res = []

        # go through nums and index
        for n, i in zip(nums, index):
            # insert num n and index i
            res.insert(i, n)

        return res