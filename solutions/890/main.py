class Solution:
    def findAndReplacePattern(self, words: list[str],
                              pattern: str) -> list[str]:

        # first normalize pattern
        pattern = self.normalize(pattern)

        # filter words by those that match normalization of pattern
        return list(filter(lambda w: self.normalize(w) == pattern, words))

    # helper method to normalize word
    def normalize(self, word: str) -> list:
        # result normalization, token mapping, and pointer
        res, mapping, ptr = [], dict(), 0

        # go thru word
        for char in word:
            # check if this char has a mapping already
            if char in mapping:
                res.append(mapping[char])
            else:
                # create it
                mapping[char] = ptr
                ptr += 1
                res.append(mapping[char])

        return res