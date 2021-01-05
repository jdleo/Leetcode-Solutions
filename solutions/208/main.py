class Trie:
    def __init__(self):
        # map for chars -> tries
        self.map = dict()
        # end token
        self.endToken = "**"

    def insert(self, word: str) -> None:
        # get reference to starting trie
        cur = self

        # go through each char
        for char in word:
            # create trie if it doesnt exist for this char
            if char not in cur.map: cur.map[char] = Trie()
            # move pointer forward
            cur = cur.map[char]

        # set end token to signal end of word
        cur.map[cur.endToken] = True

    def search(self, word: str) -> bool:
        # get reference to starting trie
        cur = self

        # go through each char
        for char in word:
            # create trie if it doesnt exist for this char
            if char not in cur.map: return False
            # move pointer forward
            cur = cur.map[char]

        # check for end token
        return cur.endToken in cur.map

    def startsWith(self, prefix: str) -> bool:
        # get reference to starting trie
        cur = self

        # go through each char
        for char in prefix:
            # create trie if it doesnt exist for this char
            if char not in cur.map: return False
            # move pointer forward
            cur = cur.map[char]

        # no problems
        return True