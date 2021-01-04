class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        # iterate thru string
        for i in range(len(s)):
            # count palindroms for both odd and even cases
            res += self.expand(s, i, i)
            res += self.expand(s, i, i + 1)

        return res

    def expand(self, s: str, i: int, j: int) -> int:
        res = 0

        # keep going while this is still a palindrome
        while i >= 0 and j < len(s) and s[i] == s[j]:
            res += 1
            i -= 1
            j += 1

        return res
