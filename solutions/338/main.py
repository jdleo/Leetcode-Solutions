class Solution:
    def countBits(self, num: int) -> List[int]:
        # dp array
        dp = [0] * (num + 1)

        # iterate from 1 to num
        for i in range(1, num + 1):
            # current num has same bits as num / 2 + the rightmost bit
            dp[i] = dp[i >> 1] + (i & 1)

        return dp