class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # to keep track of the furthest index we can reach currently
        reach = 0

        # iterate thru nums
        for i in range(len(nums) - 1):
            # update max index we can reach
            reach = max(reach, i + nums[i])

            # check if we can't proceed any further (will never be able to reach end)
            if reach == i: return False

        # check if we were able to reach the end
        return reach >= len(nums) - 1