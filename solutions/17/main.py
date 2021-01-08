class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        # create mapping of digits to letters
        letters = [
            '0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'
        ]

        # result of combinations
        res = []

        # start backtracking
        self.backtrack(res, digits, letters, 0, list())

        return res

    def backtrack(self, res, digits, letters, cur, path):
        # check if we have a valid combo
        if len(path) == len(digits):
            res.append(''.join(path))
        else:
            # go through all possible combinations of this digit mapping
            for letter in letters[ord(digits[cur]) - ord('0')]:
                # add to path
                path.append(letter)

                # backtrack
                self.backtrack(res, digits, letters, cur + 1, path)

                # remove from path
                path.pop()
