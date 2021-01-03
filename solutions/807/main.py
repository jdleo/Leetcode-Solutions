class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # total increase
        res = 0

        # dimensions
        m, n = len(grid), len(grid[0])

        # max in each row, col
        rowMax, colMax = [0] * m, [0] * n

        # go through grid
        for i in range(m):
            for j in range(n):
                # set max for this row and col
                rowMax[i] = max(rowMax[i], grid[i][j])
                colMax[j] = max(colMax[j], grid[i][j])

        # go through grid again
        for i in range(m):
            for j in range(n):
                # we can increase this building up to the min of the max of each skyline
                res += (min(rowMax[i], colMax[j]) - grid[i][j])

        return res