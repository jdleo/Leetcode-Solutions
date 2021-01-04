class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # get dimensions of matrix

        m, n = len(matrix), len(matrix[0])
        # first, flip individual rows
        for i in range(m // 2):
            matrix[i], matrix[m - i - 1] = matrix[m - i - 1], matrix[i]

        # then, flip the symmetry of individual cells
        for i in range(m):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]