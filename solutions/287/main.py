class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) > 1:
            # slow and fast pointers (to find a cycle)
            slow, fast = nums[0], nums[nums[0]]

            # go while they didnt meet
            while slow != fast:
                slow = nums[slow]
                fast = nums[nums[fast]]

            # reset fast
            fast = 0

            # go while they didnt meet again
            while slow != fast:
                # move both forward by 1
                slow = nums[slow]
                fast = nums[fast]

            return slow

        return -1