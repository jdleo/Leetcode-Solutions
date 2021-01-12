class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # character counts (for all lowercase chars)
        counts = [0] * 26

        # iter thru s and t length
        for i in range(len(s)):
            # increment for char at s, decrement for char at t
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1

        # result
        res = 0

        for c in counts:
            # simply add +count if a count is unbalanced over 0
            # we dont add for under 0 because that would be replaced with the one over 0
            if c > 0: res += c

        return res