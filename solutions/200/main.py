class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # number of islands
        res = 0

        # iterate thru grid
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # check if this is land
                if grid[i][j] == '1':
                    # this is an island, sink land connected to it
                    res += 1
                    self.sink(grid, i, j)

        return res

    # helper method to sink the islands
    def sink(self, grid, i, j):
        # bounds check
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]):
            # make sure this is land
            if grid[i][j] == '1':
                # sink the land
                grid[i][j] = '0'
                # DFS all possible directions
                for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
                    self.sink(grid, i + dy, j + dx)