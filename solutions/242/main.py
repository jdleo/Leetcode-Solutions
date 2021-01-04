class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count of characters
        counts = [0] * 26

        # go through s and fill counts
        for char in s:
            counts[ord(char) - ord('a')] += 1

        # now go through t and subtract counts
        for char in t:
            counts[ord(char) - ord('a')] -= 1

        # for them to be anagram, they have to have balanced characters
        # so all counts must be 0
        for c in counts:
            if c:
                return False

        return True