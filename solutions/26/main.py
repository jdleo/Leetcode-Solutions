class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0

        # tail of last unique seen
        tail = 0

        for i in range(1, len(nums)):
            # check if this is a NEW, unique number
            if nums[i] != nums[tail]:
                # put this unique num, one spot after last tail
                tail += 1
                nums[tail] = nums[i]

        # this is how many unique elements there are
        return tail + 1