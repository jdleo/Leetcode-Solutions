class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        # number of battle ships
        res = 0

        # iterate thru grid
        for i in range(len(board)):
            for j in range(len(board[i])):
                # check if this is a battleship
                if board[i][j] == 'X':
                    # increment count and sink this ship
                    res += 1
                    self.sink(board, i, j)

        return res

    # helper method to sink battleship
    def sink(self, board: list[list[str]], i: int, j: int):
        # bounds check
        if 0 <= i < len(board) and 0 <= j < len(board[i]):
            # check if this is even a battleship
            if board[i][j] == 'X':
                # sink it
                board[i][j] = '.'

                # go in all four possible directions
                for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
                    self.sink(board, i + dy, j + dx)