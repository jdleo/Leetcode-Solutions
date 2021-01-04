class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        # start backtracking
        self.backtrack(res, nums, list(), 0)

        return res

    def backtrack(self, res, nums, temp, start):
        # add current subset to res
        res.append(temp[:])

        # go through all possible candidates to add (from start)
        for i in range(start, len(nums)):
            # add candidate to temp
            temp.append(nums[i])
            # backtrack starting after this num we chose
            self.backtrack(res, nums, temp, i + 1)
            # remove candidate from temp
            temp.pop()