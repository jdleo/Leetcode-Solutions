class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp array size of mxn
        # filled with 1s because first col and first row only have 1 way
        dp = [[1] * n for _ in range(m)]

        # go through rest of dp
        for i in range(1, m):
            for j in range(1, n):
                # unique ways to get to THIS cell is either coming from
                # top or left
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # result is in bottom right cell
        return dp[-1][-1]
