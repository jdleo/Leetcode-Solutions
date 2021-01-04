class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        # flags for if rows are odd, or cols are odd
        odd_rows, odd_cols = [False] * n, [False] * m

        for r, c in indices:
            odd_rows[r] ^= True
            odd_cols[c] ^= True
        return sum(ro ^ cl for ro in odd_rows for cl in odd_cols)