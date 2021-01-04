class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # result array
        res = [1] * len(nums)

        # left and right products
        left = right = 1

        # go thru nums
        for i in range(len(nums)):
            # multiply by product from left and right
            res[i] *= left
            res[len(nums) - i - 1] *= right

            # multiple into left and right products
            left *= nums[i]
            right *= nums[len(nums) - i - 1]

        return res