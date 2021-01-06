class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # set for all possible permutations
        perms = set()

        # start backtracking
        self.backtrack(perms, tiles, list(), set())

        # return length of unique permutations
        # -1 because we dont want empty string perm
        return len(perms) - 1

    # helper method for backtracking permutations
    def backtrack(self, perms, tiles, temp, used):
        # add temp as string to permutations
        perms.add(''.join(temp))

        # go thru possible candidates to choose
        for i in range(len(tiles)):
            # make sure we didnt use this tile
            if i in used: continue
            # take this tile
            temp.append(tiles[i])
            used.add(i)
            # backtrack
            self.backtrack(perms, tiles, temp, used)
            # remove this tile
            temp.pop()
            used.remove(i)