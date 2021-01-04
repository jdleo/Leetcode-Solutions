class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            # simply xor this num with res
            # all numbers appear twice and x^x is always 0
            # which will leave res with the single num
            res ^= num

        return res