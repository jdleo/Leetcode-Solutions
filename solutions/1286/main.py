class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        # helper generator for combinations
        def combinations(cur, idx):
            # check if we have a valid combination
            if len(cur) == combinationLength:
                # join array to string
                yield ''.join(cur)
                return

            # go through possible characters to draw from
            for i in range(idx, len(characters)):
                # backtrack
                cur.append(characters[i])
                yield from combinations(cur, i + 1)
                cur.pop()

        # store helper attributes
        self.combos = combinations([], 0)
        self.current = True
        self.hasNextCalled = False

    def next(self) -> str:
        if self.hasNext():
            self.hasNextCalled = False
            return self.current

    def hasNext(self) -> bool:
        if self.current and not self.hasNextCalled:
            self.hasNextCalled = True
            self.current = next(self.combos, False)
        return bool(self.current)