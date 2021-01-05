class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # make deep copy of board
        grid = [[col for col in row] for row in board]

        # iterate thru board
        for i in range(len(board)):
            for j in range(len(board[i])):
                # count of live neighbors
                count = 0

                # check all directions
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        # make sure not same cell
                        if dy == 0 and dx == 0: continue
                        # bounds check
                        if 0 <= i + dy < len(board) and 0 <= j + dx < len(
                                board[i]):
                            # add live neighbors
                            count += grid[i + dy][j + dx]

                # based on rules of game of life, change board
                if count < 2: board[i][j] = 0
                elif board[i][j] and count <= 3: pass
                elif board[i][j] and count > 3: board[i][j] = 0
                elif count == 3: board[i][j] = 1