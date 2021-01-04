class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # result list
        res = []
        # start backtracking
        self.backtrack(res, nums, list())

        return res

    def backtrack(self, res, nums, temp):
        # check if we found a perm
        if len(temp) == len(nums):
            # add copy of temp to res
            res.append(temp[:])
        else:
            # go through all possibilities of nums
            for num in nums:
                # check if we already used this one
                if num in temp: continue
                # add to temp and backtrack
                temp.append(num)
                self.backtrack(res, nums, temp)
                # remove from temp
                temp.pop()