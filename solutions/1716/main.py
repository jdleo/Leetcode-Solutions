class Solution:
    def totalMoney(self, n: int) -> int:
        f, d = n // 7, n % 7
        return (49 + 7 * f) * f // 2 + (2 * f + d + 1) * d // 2
