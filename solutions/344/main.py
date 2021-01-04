class Solution:
    def reverseString(self, s: List[str]) -> None:
        # go to middle
        for i in range(len(s) // 2):
            # swap first with symmetric last
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]