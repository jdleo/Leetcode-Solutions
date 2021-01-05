class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # deep copy grid
        dp = [row[:] for row in grid]

        # minimum path for first col and first row is just running sum
        # since we can only go down and right
        for i in range(1, len(dp)):
            dp[i][0] += dp[i - 1][0]
        for j in range(1, len(dp[0])):
            dp[0][j] += dp[0][j - 1]

        # iterate thru every other cell
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                # take the min of either coming from top or left
                dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])

        # result is in bottom right of dp
        return dp[-1][-1]