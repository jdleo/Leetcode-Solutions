class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # morse code mapping (provided to us)
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]

        # set of unique morse code words
        seen = set()

        # go through each word
        for word in words:
            # current morse code representation
            cur = ''

            # go thru each char in word
            for char in word:
                # add morse code mapping to cur
                cur += morse[ord(char) - ord('a')]

            # add morse code rep to set
            seen.add(cur)

        # unique morse code words is just len of set
        return len(seen)
