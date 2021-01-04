class Solution:
    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        res = []

        # sort candidates
        candidates.sort()

        # start backtracking to fill res
        self.backtrack(res, candidates, target, 0, list())

        return res

    def backtrack(self, res, candidates, remainder, start, temp):
        # check if we exceeded target, or hit target
        if remainder < 0:
            return
        elif remainder == 0:
            res.append(temp[:])
        else:
            # go from start to end of candidates
            for i in range(start, len(candidates)):
                # simulate taking this num
                temp.append(candidates[i])

                # continue backtracking
                self.backtrack(res, candidates, remainder - candidates[i], i,
                               temp)

                # pop num we used
                temp.pop()