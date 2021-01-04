class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # total running sum
        res = 0

        # iterate through length of mat
        for i in range(len(mat)):
            # add primary diagonal
            res += mat[i][i]
            # add secondary diagonal
            res += mat[i][len(mat) - i - 1]

        # if size of matrix is odd, that means the diagonals overlapped
        # so we need to subtract that center cell
        if len(mat) % 2: res -= mat[len(mat) // 2][len(mat) // 2]
        return res
