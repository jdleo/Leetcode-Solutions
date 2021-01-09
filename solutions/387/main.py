class Solution:
    def firstUniqChar(self, s: str) -> int:
        # character count
        last = [0] * 26

        # update char counts
        for i in range(len(s)):
            last[ord(s[i]) - ord('a')] += 1

        # go through s again, and get FIRST char that is unique
        for i in range(len(s)):
            if last[ord(s[i]) - ord('a')] == 1:
                return i

        return -1