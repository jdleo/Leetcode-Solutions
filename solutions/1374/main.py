class Solution:
    def generateTheString(self, n: int) -> str:
        # if n is odd, just return n a's, if even, add a b
        return 'a' * n if n & 1 else 'a' * (n - 1) + 'b'
