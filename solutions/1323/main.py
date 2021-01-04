class Solution:
    def maximum69Number(self, num: int) -> int:
        # replace first 6 we see
        return int(str(num).replace('6', '9', 1))