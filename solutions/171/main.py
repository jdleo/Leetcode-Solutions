class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0

        # iterate backwards thru s
        for i in reversed(range(len(s))):
            # add the char at i (1 indexed) multipled by power of 26
            # where power of 26 is number of times this loop has run
            res += (ord(s[i]) - ord('A') + 1) * (26**(len(s) - 1 - i))

        return res