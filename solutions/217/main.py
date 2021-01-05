class Solution:
    # lol
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)

    # another way
    def containsDuplicate(self, nums: List[int]) -> bool:
        # set of numbers that have been seen
        seen = set()

        for num in nums:
            # check if weve already seen this num
            if num in seen: return True
            seen.add(num)

        # no problems
        return False