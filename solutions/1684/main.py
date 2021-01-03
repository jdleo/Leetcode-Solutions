class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # result of allowed strings
        res = 0
        # make allowed a set of chars for o(1) lookups
        allowed = set(allowed)

        # iterate thru words
        for word in words:
            # flag for if this word is consistent so far
            consistent = True

            # go thru char in word
            for char in word:
                # if this char is not allowed, break and set flag
                if char not in allowed:
                    consistent = False
                    break

            # if this word was consistent, increment res
            if consistent: res += 1

        return res