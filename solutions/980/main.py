class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # iterate thru grid to find starting square
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    # start backtracking
                    return self.backtrack(grid, i, j, set())

        return -1

    def backtrack(self, grid, i, j, visited):
        # visited check
        if (i, j) in visited: return 0
        # bounds check
        if not (0 <= i < len(grid) and 0 <= j < len(grid[i])): return 0
        # obstacle check
        if grid[i][j] == -1: return 0
        # check if we reached the ending square
        if grid[i][j] == 2: return 1

        # result paths
        res = 0

        # add this node to visited
        visited.add((i, j))

        # go in all possible directions
        for dy, dx in (1, 0), (0, 1), (-1, 0), (0, -1):
            res += self.backtrack(grid, i + dy, j + dx, visited)

        # remove this node to visited
        visited.remove((i, j))

        return res
