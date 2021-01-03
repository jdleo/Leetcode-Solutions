class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # result array of chars
        res = [0] * len(s)

        # go through chars, and insert at index i
        for i in range(len(s)):
            res[indices[i]] = s[i]

        # join res to string for result
        return ''.join(res)